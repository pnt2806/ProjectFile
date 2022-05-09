import cv2
import numpy as np

img = cv2.imread('breakingbad.png')
new_img = img[50:400, 250:1060]
cv2.imshow('Anh goc', img)
cv2.imshow('Anh cat', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()