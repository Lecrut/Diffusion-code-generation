from PIL import Image

def render_checkerboard(size):
    img = Image.new('RGB', size)
    pixels = img.load()
    for x in range(size[0]):
        for y in range(size[1]):
            if (x + y) % 2 == 0:
                pixels[x, y] = (255, 255, 255)
            else:
                pixels[x, y] = (0, 0, 0)
    return img

if __name__ == '__main__':
    checkerboard = render_checkerboard((8, 8))
    checkerboard.show()