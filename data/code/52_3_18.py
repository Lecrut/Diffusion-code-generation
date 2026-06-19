import math
SHAPE_RECTANGLE = 'rectangle'
SHAPE_CIRCLE = 'circle'
SHAPE_TRIANGLE = 'triangle'

def calculate_area(shape, *args):
    if shape == SHAPE_RECTANGLE:
        length, width = args
        return length * width
    elif shape == SHAPE_CIRCLE:
        radius = args[0]
        return math.pi * radius ** 2
    elif shape == SHAPE_TRIANGLE:
        base, height = args
        return 0.5 * base * height
    else:
        raise ValueError('Unsupported shape')
if __name__ == '__main__':
    rectangle_area = calculate_area(SHAPE_RECTANGLE, 6, 4)
    circle_area = calculate_area(SHAPE_CIRCLE, 3)
    triangle_area = calculate_area(SHAPE_TRIANGLE, 8, 5)
    print(f'Rectangle area: {rectangle_area}')
    print(f'Circle area: {circle_area}')
    print(f'Triangle area: {triangle_area}')