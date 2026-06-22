import cv2
import numpy as np

def draw_checkerboard(image_size, cell_size):
    rows = image_size[0] // cell_size
    cols = image_size[1] // cell_size
    board = np.zeros((image_size[0], image_size[1]), dtype=np.uint8)
    
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                cv2.rectangle(board, (j * cell_size, i * cell_size), ((j + 1) * cell_size, (i + 1) * cell_size), 255, -1)
    
    return board

if __name__ == '__main__':
    image_size = (400, 400)
    cell_size = 50
    checkerboard = draw_checkerboard(image_size, cell_size)
    cv2.imshow('Checkerboard', checkerboard)
    cv2.waitKey(0)
    cv2.destroyAllWindows()