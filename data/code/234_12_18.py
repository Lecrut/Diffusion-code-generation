from PIL import Image

def render_checkerboard(width, height):
    image = Image.new('RGB', (width, height), color='white')
    square_size = min(width, height) // 8
    for x in range(0, width, square_size):
        for y in range(0, height, square_size):
            if (x // square_size + y // square_size) % 2 == 1:
                image.paste(Image.new('RGB', (square_size, square_size), color='black'), (x, y))
    return image

if __name__ == '__main__':
    checkerboard = render_checkerboard(800, 600)
    checkerboard.show()