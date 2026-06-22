import cv2

def draw_checkerboard(image_size, cell_size):
    image = np.zeros((image_size, image_size), dtype=np.uint8)
    for i in range(0, image_size, cell_size):
        for j in range(0, image_size, cell_size):
            if (i // cell_size + j // cell_size) % 2 == 0:
                cv2.rectangle(image, (j, i), (j + cell_size, i + cell_size), (255), -1)
    return image

if __name__ == '__main__':
    image_size = 400
    cell_size = 50
    checkerboard_image = draw_checkerboard(image_size, cell_size)
    cv2.imshow('Checkerboard', checkerboard_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()