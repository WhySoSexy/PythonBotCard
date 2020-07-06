import time
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import os
import pytesseract

filename = 'Image.png'
x = 1
last_time = time.time()

while (True):
    screen = np.array(ImageGrab.grab(bbox=(581, 708, 992, 771)))
    print('loop took {} seconds'.format(time.time() - last_time))
    last_time = time.time()
    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    cv2.imwrite(filename, screen)
    x = x + 1
    print(x)
    if x == 2:
        cv2.destroyAllWindows()
        break

img = cv2.imread('Image.png')
text = pytesseract.image_to_string(img)
print(text)

index = text.find("You")
print(index)

if index == -1:
    print("ТАКОГО СЛОВА НЕТЬ!!!")
else:
    print("Я НАШЕЛЬ ЕТО СЛОВО!!!")