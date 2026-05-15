import cv2

image = cv2.imread('photos/horseman.webp')

kernel = [[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]]

def gray(image):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            r, g, b = image[i][j]
            gray_value = int(0.299 * r + 0.587 * g + 0.114 * b)
            image[i][j] = [gray_value, gray_value, gray_value]
            
def threshold(image, threshold):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            r, g, b = image[i][j]
            pixel = int(0.299 * r + 0.587 * g + 0.114 * b)
            if pixel > threshold:
                image[i][j] = [255, 255, 255]
            else:
                image[i][j] = [0, 0, 0]
                
def filter(image, kernel):
    avg = sum(map(sum, kernel))
    if avg == 0: avg = 1
    
    for i in range (1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            total = 0
            
            for k in range(3):
                for l in range(3):
                    r, g, b = image[i + k - 1][j + l - 1]
                    pixel = int(0.299 * r + 0.587 * g + 0.114 * b)
                    total += pixel * kernel[k][l]
                    
            value = total // avg
            if value < 0: value = 0
            if value > 255: value = 255
            image[i][j] = [value, value, value]


gray(image)
#cv2.imwrite('photos/horseman_gray.webp', image)

#threshold(image, 100)
#cv2.imwrite('photos/horseman_threshold.webp', image)

filter(image, kernel)
cv2.imwrite('photos/horseman_filter.webp', image)