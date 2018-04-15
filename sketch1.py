

import cv2
src = cv2.imread('cow.jpg', cv2.IMREAD_COLOR)
dst = cv2.edgePreservingFilter(src, flags=1, sigma_s=60, sigma_r=0.4)
dst = cv2.detailEnhance(src, sigma_s=10, sigma_r=0.15)

dst_gray, dst_color = cv2.pencilSketch(src, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
dst = cv2.stylization(src, sigma_s=60, sigma_r=0.07)
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()