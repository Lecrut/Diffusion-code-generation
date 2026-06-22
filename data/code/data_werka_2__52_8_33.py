import math

def validate_rectangle_args(args):
    if len(args) != 2:
        raise ValueError('Rectangle requires two parameters: width and height')
    width, height = args
    if not all((isinstance(x, (int, float)) for x in args)):
        raise ValueError('Width and height must be numbers')

def validate_circle_args(args):
    if len(args) != 1:
        raise ValueError('Circle requires one parameter: radius')
    radius = args[0]
    if not isinstance(radius, (int, float)):
        raise ValueError('Radius must be a number')

def validate_triangle_args(args):
    if len(args) != 3:
        raise ValueError('Triangle requires three parameters: base and height')
    base, height = args[:2]
    if not all((isinstance(x, (int, float)) for x in args[:2])):
        raise ValueError('Base and height must be numbers')

def calculate_area(shape_type, *args):
    if shape_type == 'rectangle':
        validate_rectangle_args(args)
        width, height = args
        return width * height
    elif shape_type == 'circle':
        validate_circle_args(args)
        radius = args[0]
        return math.pi * radius ** 2
    elif shape_type == 'triangle':
        validate_triangle_args(args)
        base, height = args[:2]
        return 0.5 * base * height
    else:
        raise ValueError(f'Unsupported shape type: {shape_type}')
if __name__ == '__main__':
    print(calculate_area('rectangle', 4, 5))
    print(calculate_area('circle', 3))
    print(calculate_area('triangle', 6, 4))
    try:
        print(calculate_area('square', 4))
    except ValueError as e:
        print(e)