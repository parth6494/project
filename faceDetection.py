import cv2
import io
import picamera
import numpy

print("Program Starting...")
cap = cv2.VideoCapture(0)
k=0
while(cap.isOpened()):
#Load a cascade file for detecting faces
    rect, image = cap.read()
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    print("Found " + str(len(faces))+" face(s)")
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
        cv2.imshow("Result", image)
        k = cv2.waitKey(10)
    if(k==27):
        break

cap.release()    
cv2.destroyAllWindows()

print("Program Ended...")
