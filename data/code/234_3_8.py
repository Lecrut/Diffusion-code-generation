from PIL import Image

def create_checkerboard(width, height, cell_size, color1=(255, 0, 0), color2=(0, 0, 255)):
    image = Image.new('RGB', (width * cell_size, height * cell_size))
    pixels = image.load()
    
    for y in range(height):
        for x in range(width):
            if (x + y) % 2 == 0:
                pixels[x * cell_size:(x + 1) * cell_size, y * cell_size:(y + 1) * cell_size] = color1
            else:
                pixels[x * cell_size:(x + 1) * cell_size, y * cell_size:(y + 1) * cell_size] = color2
    
    return image

if __name__ == '__main__':
    width = 8
    height = 6
    cell_size = 50
    checkerboard_image = create_checkerboard(width, height, cell_size)
    checkerboard_image.show()