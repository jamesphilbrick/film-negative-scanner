'''
python 3.10.1
script: film negative -> colour

take nagative image as input and return colour 
output (which may need to be manually tweaked)

James Philbrick, July 2022
'''

import numpy as np
from PIL import Image
from img_proc import *
from logs import log

# import image from 'input' folder
# 'initIm' is used for comparison and for white point 
# colour (when I expand on that feature)
IM = Image.open('./input/negative_to_process.jpg')

# swap dimensions
imDim = (IM.size[1], IM.size[0])
log('Image imported: {} of size {}, colour mode is {}'.format(IM.format, IM.size, IM.mode), newLine=True)

# convert to np array to allow for efficient processing
im = np.array(IM)

def show_image(im):
    (Image.fromarray(im)).show()

def main():
    global im, imDim
    whitePoint = np.array([255/180, 255/106, 255/78])

    im = set_white_point(im, imDim, whitePoint)
    im = invert_image(im, imDim)

    show_image(im)

if __name__=='__main__':
    main()