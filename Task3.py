# Phillip Simango - C17341516

# 1. Open image “Wartime.jpg”;
# 2. View its histogram alongside the image;
# 3. Use histogram equalisation to improve its contrast;
# 4. View the new histogram alongside the new image
# 5. Try this on a poor quality image, which channel should be equalised?

import cv2
from matplotlib import pyplot as plt

# 1. Read in the image & convert to grayscale
task3image = cv2.imread("/Users/phillipsimango/OneDrive/Wartime.html/csfiles/home_dir/wartime.jpg")
task3imageG = cv2.cvtColor(task3image, cv2.COLOR_BGR2GRAY)

# 2. Viewing the histogram alongside the image
plt.subplot(2, 2, 1)
Values = task3imageG.ravel()
plt.hist(Values, bins=256, range=[0, 256])
plt.title('Histogram A')
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

plt.subplot(2, 2, 2)
plt.imshow(task3imageG, cmap='gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])

# 4. View the new histogram alongside the new image
plt.subplot(2, 2, 3)
task3imageGeq = cv2.equalizeHist(task3imageG)  # 3. Improving contrast using histogram equalisation
Values1 = task3imageGeq.ravel()
plt.hist(Values1, bins=256, range=[0, 256])
plt.title('Histogram B')
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

plt.subplot(2, 2, 4)
plt.imshow(task3imageGeq, cmap='gray')
plt.title('Equalised Image')
plt.xticks([])
plt.yticks([])

plt.show()
cv2.waitKey()

# cv2.destroyAllWindows()
