import cv2


img = cv2.imread("anakin.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Anakin Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

path = 'anakin.jpg'
img = cv2.imread(path)

blue, green, red = cv2.split(img)

print("Color channel values: \n")
print(red,green,blue)


cv2.imshow('Blue splitted',blue)
cv2.imshow('Red splitted', red)
cv2.imshow('Green splitted', green)


an = cv2.merge((blue, green, red))
an1 = cv2.merge((blue, red, green))
an2 = cv2.merge((red, green, blue))

an_modified = cv2.merge((blue + 50, green + 50, red + 50))
an1_modified = cv2.merge((blue - 50, red - 50, green - 50))
an2_modified = cv2.merge((red - 5, green - 5, blue - 5))


cv2.imshow('anakin red', an)
cv2.imshow('anakin green', an1)
cv2.imshow('anakin blue', an2)

cv2.imshow('anakin red modified', an_modified)
cv2.imshow('anakin green modified', an1_modified)
cv2.imshow('anakin blue modified', an2_modified)

cv2.waitKey(0)
cv2.destroyAllWindows()



