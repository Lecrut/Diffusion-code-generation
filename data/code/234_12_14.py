from PIL import Image

def create_checkerboard(width, height):
    image = Image.new('L', (width, height))
    pixels = image.load()
    square_size = min(width, height) // 8
    for i in range(height):
        for j in range(width):
            if (i // square_size + j // square_size) % 2 == 0:
                pixels[j, i] = 255
            else:
                pixels[j, i] = 0
    return image

if __name__ == '__main__':
    checkerboard_image = create_checkerboard(160, 160)
    checkerboard_image.show()