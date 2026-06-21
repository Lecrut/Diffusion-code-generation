import math

def calculate_area(shape_type, *args):
    if shape_type == 'rectangle':
        if len(args) != 2:
            raise ValueError('Rectangle requires two parameters: width and height')
        return rectangle_area(*args)
    elif shape_type == 'circle':
        if len(args) != 1:
            raise ValueError('Circle requires one parameter: radius')
        return circle_area(*args)
    elif shape_type == 'triangle':
        if len(args) != 3:
            raise ValueError('Triangle requires three parameters: base and height')
        return triangle_area(*args)
    else:
        raise ValueError(f'Unsupported shape type: {shape_type}')

def rectangle_area(width, height):
    return width * height

def circle_area(radius):
    return math.pi * radius ** 2

def triangle_area(base, height):
    return 0.5 * base * height
if __name__ == '__main__':
    try:
        print(calculate_area('rectangle', 4, 5))
        print(calculate_area('circle', 3))
        print(calculate_area('triangle', 6, 4))
        print(calculate_area('square', 4))
    except ValueError as e:
        print(e)