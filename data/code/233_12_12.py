import numpy as np

def validate_dimensions(width, height):
    if not (isinstance(width, int) and isinstance(height, int)):
        raise ValueError("Width and height must be integers.")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive.")

def create_rectangle_array(width, height, symbol):
    validate_dimensions(width, height)
    return np.full((height, width), symbol, dtype=str)

def draw_rectangle(rectangle_array):
    for row in rectangle_array:
        print(''.join(row))

if __name__ == '__main__':
    rect1 = create_rectangle_array(5, 3, '*')
    draw_rectangle(rect1)
    print("-" * 10)
    rect2 = create_rectangle_array(8, 2, '#')
    draw_rectangle(rect2)
    print("-" * 10)
    rect3 = create_rectangle_array(4, 4, '@')
    draw_rectangle(rect3)