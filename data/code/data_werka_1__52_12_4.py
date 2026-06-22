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
            raise ValueError('Triangle requires three parameters: base and height')
        base, height = args[:2]
        return 0.5 * base * height
    else:
        raise ValueError(f'Invalid shape type: {shape_type}')
if __name__ == '__main__':
    try:
        print(calculate_area('rectangle', 5, 10))
        print(calculate_area('circle', 7))
        print(calculate_area('triangle', 6, 4))
        print(calculate_area('square', 4))
    except ValueError as e:
        print(e)