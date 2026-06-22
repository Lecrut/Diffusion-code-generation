RECTANGLE_WIDTH = 5
RECTANGLE_HEIGHT = 5
CHARACTER = '*'

def fill_rectangle(width=RECTANGLE_WIDTH, height=RECTANGLE_HEIGHT, char=CHARACTER):
    return [[char for _ in range(width)] for _ in range(height)]

if __name__ == '__main__':
    rectangle = fill_rectangle()
    for row in rectangle:
        print(''.join(row))