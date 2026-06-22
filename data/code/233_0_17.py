RECTANGLE_WIDTH = 5
RECTANGLE_HEIGHT = 5

def fill_rectangle(width, height):
    return [['*' for _ in range(width)] for _ in range(height)]

if __name__ == '__main__':
    rectangle = fill_rectangle(RECTANGLE_WIDTH, RECTANGLE_HEIGHT)
    for row in rectangle:
        print(''.join(row))