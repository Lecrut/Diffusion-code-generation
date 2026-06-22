from PIL import Image

def create_checkerboard(width, height, cell_size, color1, color2):
    image = Image.new('RGB', (width, height))
    pixels = image.load()
    
    for x in range(0, width, cell_size):
        for y in range(0, height, cell_size):
            if (x // cell_size + y // cell_size) % 2 == 0:
                pixels[x:y+cell_size, x:y+cell_size] = color1
            else:
                pixels[x:y+cell_size, x:y+cell_size] = color2
    
    return image

if __name__ == '__main__':
    checkerboard_image = create_checkerboard(800, 600, 50, (255, 0, 0), (0, 0, 255))
    checkerboard_image.show()