import cv2
path = "/Users/hirofumikoichihara/Desktop/ee180da/180DA-WarmUp/tokyoTower.jpg"
src = cv2.imread(path)
image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV) # or COLOR_BGR2GRAY
window_name = "Image"
cv2.imshow(window_name, image)
cv2.waitKey(0) 
  
# closing all open windows 
cv2.destroyAllWindows() 