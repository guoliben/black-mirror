import cv2

# 读取街景图
img = cv2.imread("map.png")

# 双边滤波（平滑色彩）
color = cv2.bilateralFilter(img, d=9, sigmaColor=200, sigmaSpace=200)

# 转灰度 + 边缘检测
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 7)
edges = cv2.adaptiveThreshold(blur, 255,
                              cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY, 9, 9)

# 合并色彩和边缘
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imwrite("nanjing_cartoon.jpg", cartoon)
