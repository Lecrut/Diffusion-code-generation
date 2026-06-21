import math

SHAPE_RECTANGLE = 'rectangle'
SHAPE_CIRCLE = 'circle'

def calculate_area(shape_type, dimensions):
    if shape_type == SHAPE_RECTANGLE:
        length, width = dimensions
        return length * width
    elif shape_type == SHAPE_CIRCLE:
        radius = dimensions[0]
        return math.pi * radius * radius
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle_area = calculate_area(SHAPE_RECTANGLE, (9, 6))
    circle_area = calculate_area(SHAPE_CIRCLE, (8,))
    print(rectangle_area)
    print(circle_area)