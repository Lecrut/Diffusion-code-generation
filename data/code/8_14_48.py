import math

def calculate_area(shape, *args):
    if shape == 'rectangle':
        if len(args) != 2:
            raise ValueError('Rectangle requires two arguments: width and height')
        width, height = args
        return width * height
    elif shape == 'circle':
        if len(args) != 1:
            raise ValueError('Circle requires one argument: radius')
        radius = args[0]
        return math.pi * radius ** 2
    elif shape == 'triangle':
        if len(args) != 3:
            raise ValueError('Triangle requires three arguments: base and two sides')
        base, side1, side2 = args
        s = (base + side1 + side2) / 2
        return math.sqrt(s * (s - base) * (s - side1) * (s - side2))
    else:
        raise ValueError(f'Unsupported shape: {shape}')
if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', 5, 3)
    circle_area = calculate_area('circle', 7)
    triangle_area = calculate_area('triangle', 4, 5, 6)
    print(f'Rectangle area: {rectangle_area}')
    print(f'Circle area: {circle_area}')
    print(f'Triangle area: {triangle_area}')