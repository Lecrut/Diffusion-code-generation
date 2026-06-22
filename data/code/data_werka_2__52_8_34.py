import math

def calculate_area(shape_type, *args):
    if shape_type == 'rectangle':
        if len(args) != 2:
            raise ValueError('Rectangle requires two arguments: width and height')
        width, height = args
        return width * height
    elif shape_type == 'circle':
        if len(args) != 1:
            raise ValueError('Circle requires one argument: radius')
        radius = args[0]
        return math.pi * radius ** 2
    elif shape_type == 'triangle':
        if len(args) != 3:
            raise ValueError('Triangle requires three arguments: base and two sides or base and height')
        if len(args) == 3:
            base, side1, side2 = args
            s = (base + side1 + side2) / 2
            return math.sqrt(s * (s - base) * (s - side1) * (s - side2))
        else:
            raise ValueError('Invalid arguments for triangle')
    else:
        raise ValueError(f'Unsupported shape type: {shape_type}')
if __name__ == '__main__':
    print(calculate_area('rectangle', 5, 10))
    print(calculate_area('circle', 7))
    print(calculate_area('triangle', 3, 4, 5))