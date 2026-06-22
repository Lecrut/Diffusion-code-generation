from PIL import Image

def render_checkerboard(size):
    width, height = size
    image = Image.new('RGB', (width, height), 'white')
    for x in range(width):
        for y in range(height):
            if (x + y) % 2 == 0:
                image.putpixel((x, y), (0, 0, 0))
    return image

if __name__ == '__main__':
    checkerboard = render_checkerboard((8, 8))
    checkerboard.show()