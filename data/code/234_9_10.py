import cv2
BOARD_SIZE = 8
CELL_WIDTH = 50
CELL_HEIGHT = 50

def create_checkerboard():
    image = np.zeros((BOARD_SIZE * CELL_HEIGHT, BOARD_SIZE * CELL_WIDTH, 3), dtype=np.uint8)
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            x = j * CELL_WIDTH
            y = i * CELL_HEIGHT
            if (i + j) % 2 == 0:
                cv2.rectangle(image, (x, y), (x + CELL_WIDTH, y + CELL_HEIGHT), (255, 255, 255), -1)
            else:
                cv2.rectangle(image, (x, y), (x + CELL_WIDTH, y + CELL_HEIGHT), (0, 0, 0), -1)
    return image
if __name__ == '__main__':
    checkerboard = create_checkerboard()
    cv2.imshow('Checkerboard', checkerboard)
    cv2.waitKey(0)
    cv2.destroyAllWindows()