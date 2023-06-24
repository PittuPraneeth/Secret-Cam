import cv2
import winsound
import pywhatkit
import datetime
cam = cv2.VideoCapture(0) #index of camera that cv2 has to read .here we have only one so we give 0
current_time = datetime.datetime.now()
while cam.isOpened(): #whenever cam is open we have to do something
    ret, frame1= cam.read() # frame varable read the camera
    ret, frame2 = cam.read() # frame varable read the camgera
    diff = cv2.absdiff(frame1, frame2) #here we will take the absolute difference of the two frames
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY) #we make the frame to gra color whenever there is motion
    blur = cv2.GaussianBlur(gray, (5, 5), 0) #to blur the picture
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) #to make it little bit sharper
    #dilation is jst opposite ot threshhold, threshhold is getting rid of noises and unwanted things and after that we remain with actual things wwith are interested and we make thta big for this we use dilate
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #contours is nothing but no of motions it should detect biundarues of the objects that are moving
   # cv2.drawContours(frame1, contours, -1, (0,255,0), 2) #green color border with width 2
    for c in contours:
        if cv2.contourArea(c) < 5000 : #to ignore small detection and focus on bigger ones
            continue
        x, y, w, h = cv2.boundingRect(c) # this means for every single counter yu will know what is xasxi yaxis position nd width and height
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        winsound.PlaySound('alert.wav', winsound.SND_ASYNC) #to make sound and this sound wont disturb the working of cam so we use async
        pywhatkit.sendwhatmsg("+918848661293", "someone is moving.. Be careful", current_time.hour, (current_time.minute+1))

    if cv2.waitKey(10) == ord('g'): #to turn off the cam we have to click button g . it will wait for 10ms and then turn off
        break

    cv2.imshow("Praneeth's Cam" , frame1)

# to detect the motion we will create two frames . both are comapred if both are same then no motion will be there

