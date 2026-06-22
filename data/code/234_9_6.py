import cv2
import numpy as np

def draw_checkerboard(rows, cols, cell_size):
    img = np.zeros((rows * cell_size, cols * cell_size, 3), dtype=np.uint8)
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                cv2.rectangle(img, (j * cell_size, i * cell_size), ((j + 1) * cell_size, (i + 1) * cell_size), (255, 255, 255), -1)
            else:
                cv2.rectangle(img, (j * cell_size, i * cell_size), ((j + 1) * cell_size, (i + 1) * cell_size), (0, 0, 0), -1)
    return img

if __name__ == '__main__':
    rows = 8
    cols = 8
    cell_size = 50
    checkerboard = draw_checkerboard(rows, cols, cell_size)
    cv2.imshow('Checkerboard', checkerboard)
    cv2.waitKey(0)
    cv2.destroyAllWindows()