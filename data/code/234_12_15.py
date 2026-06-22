from PIL import Image

def render_checkerboard(size):
    width, height = size
    image = Image.new('RGB', (width, height), 'white')
    for x in range(0, width, 2):
        for y in range(0, height, 2):
            if (x // 2 + y // 2) % 2 == 0:
                image.putpixel((x, y), (0, 0, 0))
                image.putpixel((x + 1, y), (0, 0, 0))
                image.putpixel((x, y + 1), (0, 0, 0))
                image.putpixel((x + 1, y + 1), (0, 0, 0))
    return image

if __name__ == '__main__':
    checkerboard = render_checkerboard((8, 8))
    checkerboard.show()