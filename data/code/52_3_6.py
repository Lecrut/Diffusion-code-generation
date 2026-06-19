import math

SHAPE_RECTANGLE = 'rectangle'
SHAPE_CIRCLE = 'circle'
SHAPE_TRIANGLE = 'triangle'

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_area(shape, *args):
    if shape == SHAPE_RECTANGLE:
        length, width = args
        return calculate_rectangle_area(length, width)
    elif shape == SHAPE_CIRCLE:
        radius = args[0]
        return calculate_circle_area(radius)
    elif shape == SHAPE_TRIANGLE:
        base, height = args
        return calculate_triangle_area(base, height)
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle_area = calculate_area(SHAPE_RECTANGLE, 5, 3)
    circle_area = calculate_area(SHAPE_CIRCLE, 4)
    triangle_area = calculate_area(SHAPE_TRIANGLE, 6, 2)
    print(f"Rectangle area: {rectangle_area}")
    print(f"Circle area: {circle_area}")
    print(f"Triangle area: {triangle_area}")