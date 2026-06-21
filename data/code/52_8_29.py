import math

def calculate_area(shape_type, *args):
    if shape_type == 'rectangle':
        if len(args) != 2:
            raise ValueError('Rectangle requires two parameters: width and height')
        width, height = args
        return width * height
    elif shape_type == 'circle':
        if len(args) != 1:
            raise ValueError('Circle requires one parameter: radius')
        radius = args[0]
        return math.pi * radius ** 2
    elif shape_type == 'triangle':
        if len(args) != 3:
            raise ValueError('Triangle requires three parameters: base, height, and side length')
        base, height, side_length = args
        area = base * height / 2
        return area
    else:
        raise ValueError(f'Unsupported shape type: {shape_type}')
if __name__ == '__main__':
    try:
        print(calculate_area('rectangle', 5, 10))
        print(calculate_area('circle', 7))
        print(calculate_area('triangle', 6, 4, 5))
        print(calculate_area('square', 4))
    except ValueError as e:
        print(e)