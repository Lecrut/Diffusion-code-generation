import cv2
import numpy as np

def draw_checkerboard(rows, cols, cell_size):
    if rows <= 0 or cols <= 0 or cell_size <= 0:
        raise ValueError('Rows, columns, and cell size must be positive integers.')
    img_width = cols * cell_size
    img_height = rows * cell_size
    image = np.zeros((img_height, img_width, 3), dtype=np.uint8)
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                color = [255, 255, 255]
            else:
                color = [0, 0, 0]
            x_start = j * cell_size
            y_start = i * cell_size
            cv2.rectangle(image, (x_start, y_start), (x_start + cell_size, y_start + cell_size), color, -1)
    return image
if __name__ == '__main__':
    rows = 8
    cols = 8
    cell_size = 50
    try:
        checkerboard_image = draw_checkerboard(rows, cols, cell_size)
        cv2.imshow('Checkerboard', checkerboard_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except ValueError as e:
        print(e)