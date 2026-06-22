import cv2
import numpy as np

def draw_checkerboard(rows, cols, cell_size):
    board = np.zeros((rows * cell_size, cols * cell_size), dtype=np.uint8)
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                cv2.rectangle(board, (j * cell_size, i * cell_size), ((j + 1) * cell_size, (i + 1) * cell_size), (255), -1)
    return board

if __name__ == '__main__':
    rows = 8
    cols = 8
    cell_size = 64
    checkerboard = draw_checkerboard(rows, cols, cell_size)
    cv2.imshow('Checkerboard', checkerboard)
    cv2.waitKey(0)
    cv2.destroyAllWindows()