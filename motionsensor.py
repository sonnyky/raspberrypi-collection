import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

while True:
    i=GPIO.input(7)
    if i==0:
        print "No one"
    elif i==1:
        print "Someone is here"
    time.sleep(0.1)
