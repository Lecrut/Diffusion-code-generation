from PIL import Image

def create_checkerboard(width, height, cell_size, color1, color2):
    image = Image.new('RGB', (width * cell_size, height * cell_size))
    pixels = image.load()
    for row in range(height):
        for col in range(width):
            if (row + col) % 2 == 0:
                pixels[col * cell_size:(col + 1) * cell_size, row * cell_size:(row + 1) * cell_size] = color1
            else:
                pixels[col * cell_size:(col + 1) * cell_size, row * cell_size:(row + 1) * cell_size] = color2
    return image

if __name__ == '__main__':
    checkerboard_image = create_checkerboard(8, 8, 50, (255, 0, 0), (0, 0, 255))
    checkerboard_image.save('checkerboard.png')
    checkerboard_image.show()