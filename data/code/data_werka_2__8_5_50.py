import math
SHAPE_RECTANGLE = 'rectangle'
SHAPE_CIRCLE = 'circle'
SHAPE_TRIANGLE = 'triangle'

def calculate_area(shape):
    shape_type = shape.get('type')
    if shape_type == SHAPE_RECTANGLE:
        width = shape.get('width', 0)
        height = shape.get('height', 0)
        return rectangle_area(width, height)
    elif shape_type == SHAPE_CIRCLE:
        radius = shape.get('radius', 0)
        return circle_area(radius)
    elif shape_type == SHAPE_TRIANGLE:
        base = shape.get('base', 0)
        height = shape.get('height', 0)
        return triangle_area(base, height)
    else:
        raise ValueError(f'Unsupported shape type: {shape_type}')

def rectangle_area(width, height):
    return width * height

def circle_area(radius):
    return math.pi * radius ** 2

def triangle_area(base, height):
    return 0.5 * base * height
if __name__ == '__main__':
    rectangle = {'type': SHAPE_RECTANGLE, 'width': 6, 'height': 12}
    circle = {'type': SHAPE_CIRCLE, 'radius': 8}
    triangle = {'type': SHAPE_TRIANGLE, 'base': 10, 'height': 5}
    print('Rectangle area:', calculate_area(rectangle))
    print('Circle area:', calculate_area(circle))
    print('Triangle area:', calculate_area(triangle))