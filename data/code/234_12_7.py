from PIL import Image

def render_checkerboard(size):
    width, height = size
    image = Image.new('RGB', (width, height), 'white')
    for x in range(width):
        for y in range(height):
            if (x + y) % 2 == 0:
                color = 'black'
            else:
                color = 'white'
            image.putpixel((x, y), color)
    return image

if __name__ == '__main__':
    checkerboard_image = render_checkerboard((8, 8))
    checkerboard_image.show()