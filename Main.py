import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread('img4.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
x, y, w, h = cv2.boundingRect(opening)

if (x, y, w, h) != (0, 0, 0, 0):
    print(x, y, w, h)

cv2.rectangle(img, (x, y), (x+w, y + h), (0, 255, 0), 3)
cv2.circle(img, (int(x+w/2), int(y+h/2)), 5, (0, 0, 255), -1)

# res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
# Webcamera no 0 is used to capture the frames
cap = cv2.VideoCapture(0)

# This drives the program into an infinite loop.
while (1):
    # Captures the live stream frame-by-frame
    _, frame = cap.read()
    # Converts images from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Here we are defining range of bluecolor in HSV
    # This creates a mask of blue coloured
    # objects found in the frame.
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # The bitwise and of the frame and mask is done so
    # that only the blue coloured objects are highlighted
    # and stored in res
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    # This displays the frame, mask
    # and res which we created in 3 separate windows.
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()

# release the captured frame
cap.release()
'''

# https://www.instructables.com/Servo-Motor-Control-With-Raspberry-Pi/
# https://www.youtube.com/watch?v=ZEg2IjACG9s
# https://www.raspberrypi.org/blog/how-to-control-multiple-servo-motors-with-raspberry-pi/    for angles

