import math

def calculate_area(shape, dimensions):
    if shape == 'rectangle':
        length, width = dimensions
        return length * width
    elif shape == 'circle':
        radius = dimensions[0]
        return math.pi * radius ** 2
    elif shape == 'triangle':
        base, height = dimensions
        return 0.5 * base * height
    else:
        raise ValueError('Unsupported shape')
if __name__ == '__main__':
    rectangle_dimensions = (5, 3)
    circle_dimensions = (4,)
    triangle_dimensions = (6, 2)
    print('Rectangle area:', calculate_area('rectangle', rectangle_dimensions))
    print('Circle area:', calculate_area('circle', circle_dimensions))
    print('Triangle area:', calculate_area('triangle', triangle_dimensions))