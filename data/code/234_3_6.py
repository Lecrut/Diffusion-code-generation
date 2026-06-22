from PIL import Image

def create_checkerboard(width, height, cell_size, color1, color2):
    image = Image.new('RGB', (width, height))
    pixels = image.load()
    
    for y in range(height):
        for x in range(width):
            if (x // cell_size + y // cell_size) % 2 == 0:
                pixels[x, y] = color1
            else:
                pixels[x, y] = color2
    
    return image

if __name__ == '__main__':
    checkerboard = create_checkerboard(400, 300, 50, (255, 0, 0), (0, 0, 255))
    checkerboard.show()