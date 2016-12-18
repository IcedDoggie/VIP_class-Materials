"""
coinCounting.py

YOUR WORKING FUNCTION

"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

# you are allowed to import other Python packages above
##########################

def coinCount(coinMat, i):
	# Inputs
	# coinMat: 4-D numpy array of row*col*3*numImages, 
	#  numImage denote number of images in coin set (10 in this case)
	# i: coin set image number (1, 2, ... 10)
	# Output
	# ans: Total value of the coins in the image, in float type
	#
	#########################################################################
	# ADD YOUR CODE BELOW THIS LINE

	######## Loading #######
	string_for_image = coinMat + "_" + str(i) + '.jpg'
	coin_image_gray = cv2.imread(string_for_image, cv2.IMREAD_GRAYSCALE)
	coin_image = cv2.imread(string_for_image)
	########################

	######## Thresholding #########
	retOtsu, threshOtsu = cv2.threshold(coin_image_gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)
	retOtsu, threshOtsu_noInv = cv2.threshold(coin_image_gray, 0, 255, cv2.THRESH_OTSU) #for concatenation
	#############################

	######## Morphological Ops #########
	kernel = np.ones((6,6),np.uint8)
	morphOpen = cv2.morphologyEx(threshOtsu, cv2.MORPH_OPEN, kernel)
	morph_to_be_parsed = morphOpen
	####################################
	
	######## Edge Detection(Currently Not Used) ###########
	canny_edge_detector = cv2.Canny(morphOpen, retOtsu, 255)
	###################################

	########### Find Contours ###########
	contours_image, contours, hierarchy = cv2.findContours(morph_to_be_parsed
		, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	#####################################

	########### Find Rectangles for edges #############
	for cnt in contours:
		x,y,w,h = cv2.boundingRect(cnt)
		###### Remove possible noises #######
		print(str(x) + " " + str(y) + " " + str(x+w) + " " + str(y+h))
		if w >= 20 and h >= 30:   # the minimum width to be considered a coin
			cv2.rectangle(coin_image, (x, y), (x+w, y+h), (255, 0, 0), 2)
	###################################################

	plt.subplot(231), plt.imshow(threshOtsu, cmap = 'gray')
	plt.title('Thresholded Image For Otsu'), plt.xticks([]), plt.yticks([])
	# plt.subplot(232), plt.hist(coin_image.ravel(), 256, [0, 256])
	plt.subplot(232), plt.imshow(morphOpen, cmap = 'gray')
	plt.title('morphOpen'), plt.xticks([]), plt.yticks([])
	plt.subplot(233), plt.imshow(canny_edge_detector, cmap = 'gray')
	plt.title('Canny Edge Detector'), plt.xticks([]), plt.yticks([])
	# plt.subplot(234), plt.imshow(contours_image, cmap = 'gray')
	plt.subplot(234), plt.imshow(coin_image, cmap = 'gray')
	plt.title('Bounding Box'), plt.xticks([]), plt.yticks([])
	plt.subplot(235), plt.imshow(contours_image, cmap = 'gray')
	plt.title('Contour Image'), plt.xticks([]), plt.yticks([])
	plt.show()
	#############################


	# END OF YOUR CODE
	#########################################################################
	# return ans

coinCount("coin_s1", 4)

