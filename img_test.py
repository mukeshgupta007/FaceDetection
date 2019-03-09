import cv2
cam=cv2.VideoCapture(0)
fd=cv2.CascadeClassifier(r'C:\Users\hp\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
while True:
    r,i=cam.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    face=fd.detectMultiScale(j)
    print('no. of faces are:',len(face))
    if(len(face)>0):
        for(x,y,w,h) in face:
            cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,255),5)
            cv2.imshow('image',i)
            k=cv2.waitKey(3)
            if(k==ord('q')):
                cv2.destroyAllWindows()
                break
