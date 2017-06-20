from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return 'Yummy Cakes!'

@app.route('/pinhigh/<number>')
def pinHigh(number):
    pinNum = int(number)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinNum, GPIO.OUT)
    GPIO.output(pinNum, GPIO.HIGH)
    return render_template('pinHigh.html', number=number)

@app.route('/pinlow/<number>')
def pinLow(number):
    pinNum = int(number)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinNum, GPIO.OUT)
    GPIO.output(pinNum, GPIO.HIGH)
    return render_template('pinLow.html', number=number)

@app.route('/pintoggle/<number>')
def pinCtrl(number):
    pinNum = int(number)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinNum, GPIO.OUT)
    newState = not GPIO.input(pinNum)
    GPIO.output(pinNum, newState)
    return render_template('pinToggle.html', number=number, state=newState)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
