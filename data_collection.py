import numpy as np
import mediapipe as mp
import cv2

cap = cv2.VideoCapture(1)

while True:
    _, frm = cap.read()
    cv2.imshow("window", frm)

    if cv2.waitkey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break