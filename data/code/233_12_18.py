import numpy as np

SYMBOL = '*'
SPACE = ' '

def create_rectangle(width, height):
    rectangle_array = np.full((height, width), SYMBOL)
    return rectangle_array

def print_rectangle(rectangle_array):
    for row in rectangle_array:
        print(''.join(row))

if __name__ == '__main__':
    rect1 = create_rectangle(5, 3)
    print_rectangle(rect1)
    print("-" * 10)
    rect2 = create_rectangle(8, 2)
    print_rectangle(rect2)
    print("-" * 10)
    rect3 = create_rectangle(4, 4)
    print_rectangle(rect3)