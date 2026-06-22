from PIL import Image
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def render_checkerboard(size):
    checkerboard_image = Image.new('RGB', (size, size))
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            checkerboard_image.putpixel((j, i), color)
    return checkerboard_image
if __name__ == '__main__':
    board_size = 8
    img = render_checkerboard(board_size)
    img.save('checkerboard.png')
    print(f'Checkerboard image size: {img.size}')