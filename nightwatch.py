# Project Nightwatch
# Team Members: Andrew Burrell, Kyle Jenko, Brandon Kim, Humberto Ruiz

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) 
GPIO.setup(11,GPIO.OUT) #Cam Servo PWM
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #Camera tilt up
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #Camera tilt down
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #Open payload clamp
GPIO.setup(13,GPIO.OUT)
cam_servo= GPIO.PWM(11,50) #camera servo pin 11
cam_servo.start(0)
clamp_servo = GPIO.PWM(13,50) #clamp servo pin 13
clamp_servo.start(0)
while True:
    # Tilt Camera up
    if GPIO.input(16) == GPIO.HIGH:
        print('Tilting up') #Microservo
        cam_servo.ChangeDutyCycle(5.5)
        time.sleep(.1)
    # Tilt camera down
    if GPIO.input(18) == GPIO.HIGH:
        print('Tilting down') #Microservo
        cam_servo.ChangeDutyCycle(10.5)
        time.sleep(1.5)
    # Release payload
    if GPIO.input(22) == GPIO.HIGH:
        print("Bombs Away!")
        clamp_servo.ChangeDutyCycle(2.5)
        print("Opening clamp")
        time.sleep(.1)
        
        clamp_servo.ChangeDutyCycle(0)
        time.sleep(1)
        print("Closing clamp")
        clamp_servo.ChangeDutyCycle(7.5)
        time.sleep(.215)
        clamp_servo.ChangeDutyCycle(0)
    
