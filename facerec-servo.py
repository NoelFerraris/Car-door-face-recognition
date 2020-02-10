from picamera.array import PiRGBArray
from picamera import picamera
import time as Time 
import cv2
import sys
import imutils
import RPi.GPIO as GPIO
servo1 = 12
servo2 = 10

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo1, GPIO.OUT)

GPIO.setup(servo2, GPIO.OUT)

s1 = GPIO.PWM(servo1, 50)
s2 = GPIO.PWM(servo2, 50)
s1.start(7.5)
s2.start(7.5)

cascPath = sys.argv[0] #Get user supplied value

faceCascade = cv2.CascadeClassifier('haarcascade frontalface default.xml') # Create haar Casscade

camera = picamera ()
camera = (160,120)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size= (160,120))# initialize the camera and grab reference to the raw camera capture

Time.sleep(.1)
lastTime = Time.time()*1000.0

for frame in camera.capture_continous(rawCapture, format"bgr", use_video_port=True):

    frame = frame.array
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors=5, minSize(30, 30),) #DETECT FACE IN IMAGE

    print ("Found {0} faces!".format(len(faces)))
    lastTime = Time.time()*1000.0
    for (x,y,w,h) in faces:
        color = (255,0,0)
        stroke = 2
        end_cordx = x + w
        end_cordy= y + h
        cv2.rectangle(frame, (x,y), (end_cordx, end_cordy), color, stroke)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("q"):
        break

    if (len(faces)): #once faces are detected this moves the two servos simultaneously
        positionl = 12
        positionr = 12
        s1.ChangeDutyCycle(positionl)
        s2.ChangeDutyCycle(positionr)
        time.sleep(1)

