from PIL import Image

def create_checkerboard(size):
    image = Image.new('RGB', (size * 2, size * 2), 'white')
    draw = image.load()
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                draw[i * 2, j * 2] = (0, 0, 0)
                draw[(i * 2) + 1, j * 2] = (0, 0, 0)
                draw[i * 2, (j * 2) + 1] = (0, 0, 0)
                draw[(i * 2) + 1, (j * 2) + 1] = (0, 0, 0)
            else:
                draw[i * 2, j * 2] = (255, 255, 255)
                draw[(i * 2) + 1, j * 2] = (255, 255, 255)
                draw[i * 2, (j * 2) + 1] = (255, 255, 255)
                draw[(i * 2) + 1, (j * 2) + 1] = (255, 255, 255)
    return image

if __name__ == '__main__':
    size = 8
    checkerboard_image = create_checkerboard(size)
    checkerboard_image.show()