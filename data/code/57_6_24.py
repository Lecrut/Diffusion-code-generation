import math

def calculate_area(shape_type, dimensions):
    if shape_type == 'rectangle':
        length, width = dimensions
        return length * width
    elif shape_type == 'circle':
        radius = dimensions[0]
        return math.pi * radius ** 2
    elif shape_type == 'triangle':
        base, height = dimensions
        return 0.5 * base * height
    else:
        raise ValueError(f'Unsupported shape type: {shape_type}')
if __name__ == '__main__':
    rectangle_dimensions = (5, 10)
    circle_dimensions = (7,)
    triangle_dimensions = (8, 6)
    print('Rectangle area:', calculate_area('rectangle', rectangle_dimensions))
    print('Circle area:', calculate_area('circle', circle_dimensions))
    print('Triangle area:', calculate_area('triangle', triangle_dimensions))