from PIL import Image

def create_checkerboard(width, height, cell_size, color1, color2):
    image = Image.new('RGB', (width, height))
    for y in range(0, height, cell_size):
        for x in range(0, width, cell_size):
            if (x // cell_size + y // cell_size) % 2 == 0:
                image.paste(color1, (x, y, x + cell_size, y + cell_size))
            else:
                image.paste(color2, (x, y, x + cell_size, y + cell_size))
    return image

if __name__ == '__main__':
    checkerboard = create_checkerboard(800, 600, 50, (255, 0, 0), (0, 0, 255))
    checkerboard.show()