from PIL import Image

def create_checkerboard(width, height, cell_size, color1, color2):
    checkerboard = Image.new('RGB', (width, height))
    for y in range(0, height, cell_size):
        for x in range(0, width, cell_size):
            if (x // cell_size + y // cell_size) % 2 == 0:
                checkerboard.paste(color1, (x, y, x + cell_size, y + cell_size))
            else:
                checkerboard.paste(color2, (x, y, x + cell_size, y + cell_size))
    return checkerboard

if __name__ == '__main__':
    width = 800
    height = 600
    cell_size = 50
    color1 = (255, 0, 0)
    color2 = (0, 255, 0)
    checkerboard = create_checkerboard(width, height, cell_size, color1, color2)
    checkerboard.save('checkerboard.png')