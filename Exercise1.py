import cv2
import numpy as np
from PIL import Image
import numpy.matlib



image = cv2.imread('C:/Users/pavan\Downloads/R.png')
image_matrix = np.array(image)
cv2.imshow("Image",image)
cv2.waitKey(0)
length = len(image_matrix) 
width = len(image_matrix[0])
Grayscale_matrix = np.zeros((length,width))

for row in range(len(image_matrix)):
    for col in range(len(image_matrix[row])):
        (Red,Green,Blue) = image_matrix[row][col]
        Grayscale_matrix[row][col]=(Red+Green+Blue) *0.33 
cv2.imshow('Grayscale_manual',Grayscale_matrix) 
cv2.waitKey(0) 





GrayscaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale',GrayscaleImage) 
cv2.waitKey(0) 


cv2.destroyAllWindows()
 # Grayscale to rgb
 #Grayscale=0.2989⋅Red+0.5870⋅Green+0.1140⋅Blue

 #from rgb to cmyk


