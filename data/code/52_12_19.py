import math
SHAPE_RECTANGLE = 'rectangle'
SHAPE_CIRCLE = 'circle'
SHAPE_TRIANGLE = 'triangle'
ERROR_PREFIX = 'Invalid parameters for '

def calculate_area(shape_type, **kwargs):
    if shape_type == SHAPE_RECTANGLE:
        width = kwargs.get('width')
        height = kwargs.get('height')
        if width is None or height is None:
            raise ValueError(ERROR_PREFIX + SHAPE_RECTANGLE + ': width and height are required')
        return width * height
    elif shape_type == SHAPE_CIRCLE:
        radius = kwargs.get('radius')
        if radius is None:
            raise ValueError(ERROR_PREFIX + SHAPE_CIRCLE + ': radius is required')
        return math.pi * radius ** 2
    elif shape_type == SHAPE_TRIANGLE:
        base = kwargs.get('base')
        height = kwargs.get('height')
        if base is None or height is None:
            raise ValueError(ERROR_PREFIX + SHAPE_TRIANGLE + ': base and height are required')
        return 0.5 * base * height
    else:
        raise ValueError(f'Unsupported shape type: {shape_type}')
if __name__ == '__main__':
    try:
        print(calculate_area(SHAPE_RECTANGLE, width=5, height=10))
        print(calculate_area(SHAPE_CIRCLE, radius=7))
        print(calculate_area(SHAPE_TRIANGLE, base=6, height=4))
        print(calculate_area('square', side=3))
    except ValueError as e:
        print(e)