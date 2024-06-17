import cv2
import time
height = 640
width = 360
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 120)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

fps_start_time = time.time()
fps_count = 0
fps = 0

faceCascade = cv2.CascadeClassifier('AI Git\HAAR\haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('AI Git\HAAR\haarcascade_eye.xml')
while True:
    ignore, frame = cam.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray, 1.3, 5)
    eyes = eyeCascade.detectMultiScale(frameGray, 1.3, 5)
    for eye in eyes:
        Xe,Ye, We, He = eye
        cv2.rectangle(frame, (Xe,Ye), (Xe+We, Ye+He), (0, 0 ,255), 3)
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame, (x,y),(x+w, y+h), (255, 0, 0), 3)
    fps_count += 1
    if time.time() - fps_start_time >= 1:
        fps = fps_count
        fps_count = 0
        fps_start_time = time.time()
    cv2.rectangle(frame, (20, 100), (170, 60), (0, 0, 255), 2)
    cv2.putText(frame, f'FPS: {fps}', (30, 90), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
        
    cv2.imshow('Webcam 1', frame)
    
    cv2.moveWindow('Webcam 1', 0,0)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()