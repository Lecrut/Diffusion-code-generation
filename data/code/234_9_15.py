import cv2
import numpy as np

def draw_checkerboard(width, height, cell_size):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(0, height, cell_size):
        for j in range(0, width, cell_size):
            if (i // cell_size + j // cell_size) % 2 == 0:
                cv2.rectangle(img, (j, i), (j + cell_size, i + cell_size), (255, 255, 255), -1)
    return img

if __name__ == '__main__':
    width = 800
    height = 600
    cell_size = 50
    checkerboard = draw_checkerboard(width, height, cell_size)
    cv2.imshow('Checkerboard', checkerboard)
    cv2.waitKey(0)
    cv2.destroyAllWindows()