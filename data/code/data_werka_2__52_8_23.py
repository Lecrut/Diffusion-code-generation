import math

def calculate_area(shape_type, *args):
    if shape_type == 'rectangle':
        if len(args) != 2:
            raise ValueError('Rectangle requires two parameters: width and height')
        width, height = args
        area = width * height
        return area
    elif shape_type == 'circle':
        if len(args) != 1:
            raise ValueError('Circle requires one parameter: radius')
        radius, = args
        area = math.pi * radius ** 2
        return area
    elif shape_type == 'triangle':
        if len(args) != 3:
            raise ValueError('Triangle requires three parameters: base and height')
        base, height = args[:2]
        area = 0.5 * base * height
        return area
    else:
        raise ValueError(f'Unsupported shape type: {shape_type}')
if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', 4, 5)
    circle_area = calculate_area('circle', 3)
    triangle_area = calculate_area('triangle', 6, 2)
    print(f'Rectangle area: {rectangle_area}')
    print(f'Circle area: {circle_area}')
    print(f'Triangle area: {triangle_area}')