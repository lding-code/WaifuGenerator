import cv2
import numpy as np 
import matplotlib.pyplot as plt
import os

pathIn = "./data/raw/"
pathOut = "./data/target/"

names = os.listdir(pathIn)

for index in range(len(names)):
    img = cv2.imread(pathIn + names[index])
    cv2.imwrite(pathOut + "{}.jpg".format(index), img)