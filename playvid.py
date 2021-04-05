import numpy as np
import cv2
import time

cap = cv2.VideoCapture('driving.mp4')
leftcircle = 50
playbackdelay = 0.01

while(cap.isOpened()):
    ret, frame = cap.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Add circle and text to frame
    frame = cv2.circle(frame,(leftcircle,500), 30, (0,0,255), 3)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Tracking Vehicle @ ['+str(leftcircle)+']',(10,50), font, 1,(0,0,255),2,cv2.LINE_AA)
   
    if leftcircle < 720:
        leftcircle = leftcircle +4


    cv2.imshow('frame',frame)
    time.sleep(playbackdelay)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()