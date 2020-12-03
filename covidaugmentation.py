from os import path
import numpy as np
from os import listdir,makedirs
import cv2
import os
import cv2
import numpy as np
from skimage import io
from skimage.transform import rotate, AffineTransform, warp
import matplotlib.pyplot as plt
import random
from skimage import img_as_ubyte
import os
i=1
from skimage.util import random_noise
dstpath = "coviddataset" # Destination Folder
try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in same folder")

for folder in os.listdir("liverdata2020"):

    if(folder == ".DS_Store"):
        continue

    # Loop through each category
    for filename in os.listdir(path.join("coviddataset", folder)):
        # Select images which are png and jpg only
        if (filename[-3:] == "png" or filename[-3:] == "jpg"or filename[-4:] == "jpeg"):
            # Get full image by joining
            # all the path to the image
            if i>20:
                i=1
            image = path.join("coviddataset", folder, filename)
            # Use open cv to read the image
            img = cv2.imread(image)
            img=cv2.resize(img,(224,224))
            height,weight=img.shape[:2]
            rotat_matrix2=cv2.getRotationMatrix2D((weight/2,height/2),i,1)
            rotat_img2=cv2.warpAffine(img,rotat_matrix2,(weight,height))
            rotat_matrix3 = cv2.getRotationMatrix2D((weight / 2, height / 2), i-3, 1)
            rotat_img3 = cv2.warpAffine(img, rotat_matrix3, (weight, height))
            # Resize the image to (64, 128)
            i=i+1
            # Default for hog
            imgfr = np.fliplr(img)
            noise_img = random_noise(img, mode='s&p', amount=0.02)
            noise_img = np.array(255 * noise_img, dtype='uint8')
            #gosimg=random_noise(img, mode='gaussian', seed=None, clip=True)
            #gusinmg = np.array(255 * gosimg, dtype='uint8' ,amount=0.02)
            #r_image = rotate(img, angle=20)
            cv2.imwrite(os.path.join(dstpath,folder,"rotation"+filename), rotat_img2)
            cv2.imwrite(os.path.join(dstpath, folder, "rotation3" + filename), rotat_img3)
            cv2.imwrite(os.path.join(dstpath, folder, "nosie" + filename), noise_img)
            #cv2.imwrite(os.path.join(dstpath, folder, "gnosie" + filename), gusinmg)
            cv2.imwrite(os.path.join(dstpath, folder, "flipr" + filename), imgfr)
            print("saving image")
