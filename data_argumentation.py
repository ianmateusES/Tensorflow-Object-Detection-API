"""
# Author: narenltk
# Date: 24/04/2020
#
## Some of the code that I reffered has been from opencv-python documentation page
## https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html
"""

# Import packages
import cv2
from pathlib import Path
import glob
import random
import imutils

def flip_image(file_path,resize_file_path,extension):
	'''
        :param file_path: contains image dir
	:param resize_file_path: destination dir
	:param extension: image extension
	'''
	path = glob.glob(file_path+"/*"+extension)
	i = 1
	for image in path:
		img=cv2.imread(str(image))
		horizontal_img = cv2.flip( img, 0 )
		cv2.imwrite(resize_file_path+"/horizontal_flip-2"+"("+str(i)+")"+extension ,horizontal_img)
		vertical_img = cv2.flip( img, 1 )
		cv2.imwrite(resize_file_path+"/vertical_flip-2"+"("+str(i)+")"+extension ,vertical_img)
		both_img = cv2.flip( img, -1 )
		cv2.imwrite(resize_file_path+"/both_filp-2"+"("+str(i)+")"+extension ,both_img)
		i = i+1

flip_image("D:\objdetection\mask_dataset","D:\objdetection\mask_dataset\output",".jpg")

"""
def resize_image(file_path,w,h,resize_file_path,extension):
	'''
        :param file_path: contains image dir
        :param w: width of resize image 
	:param h: height of resize image
	:param resize_file_path: destination dir
	:param extension: image extension
	'''
	path = glob.glob(file_path+"/*"+extension)
	i = 1
	for image in path:
		img=cv2.imread(str(image))
		img=cv2.resize(img,(w,h))
		cv2.imwrite(resize_file_path+"/Resize-2"+str(w)+"*"+str(h)+"("+str(i)+")"+extension, img)
		i = i+1


resize_image("red",1024,636,"red",".jpg")

def gray_scale(file_path,resize_file_path,extension):
	'''
        :param file_path: contains image dir        
	:param resize_file_path: destination dir
	:param extension: image extension
	'''
	path = glob.glob(file_path+"/*"+extension)
	i = 1
	for image in path:
		img=cv2.imread(str(image))
		img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		cv2.imwrite(resize_file_path+"/gray_scaled-"+"("+str(i)+")"+extension ,img)
		i = i+1

# gray_scale("image","image",".jpg")

def sp_noise(file_path,resize_file_path,extension,prob):
	'''
        :param file_path: contains image dir
	:param resize_file_path: destination dir
	:param extension: image extension
	:param prob: Probability of the noise
	'''

	path = glob.glob(file_path+"/*"+extension)
	i = 1
	for image in path:
		img=cv2.imread(str(image),0)
		output = np.zeros(img.shape,np.uint8)
		thres = 1 - prob
		for i in range(img.shape[0]):
			for j in range(img.shape[1]):
				rdn = random.random()
				if rdn < prob:
					output[i][j] = 0
				elif rdn > thres:
					output[i][j] = 255
				else:
					output[i][j] = img[i][j]
		cv2.imwrite(resize_file_path+"/noisy-2"+"("+str(i)+")"+extension ,output)
		i = i+1

# sp_noise("red","red/red",".jpg",0.02)

def rotate_image(file_path,resize_file_path,extension,angle):
	'''
        :param file_path: contains image dir
	:param resize_file_path: destination dir
	:param extension: image extension
	:param angle: angle of rotation
	'''
	path = glob.glob(file_path+"/*"+extension)
	i = 1
	for image in path:
		img=cv2.imread(str(image))
		rotated = imutils.rotate(img, angle)
		cv2.imwrite(resize_file_path+"/rotated-2"+str(angle)+"("+str(i)+")"+extension ,img)
		i = i+1

rotate_image("D:\objdetection\mask_dataset","D:\objdetection\mask_dataset\output",".jpg",270)
"""

