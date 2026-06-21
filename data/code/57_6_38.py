import math

def calculate_area(shape, dimensions):
    if shape == 'rectangle':
        return _calculate_rectangle_area(dimensions)
    elif shape == 'circle':
        return _calculate_circle_area(dimensions)
    else:
        raise ValueError(f'Unsupported shape: {shape}')

def _calculate_rectangle_area(dimensions):
    if len(dimensions) != 2:
        raise ValueError('Rectangle requires exactly two dimensions')
    length, width = dimensions
    return length * width

def _calculate_circle_area(dimensions):
    if len(dimensions) != 1:
        raise ValueError('Circle requires exactly one dimension (radius)')
    radius = dimensions[0]
    return math.pi * radius ** 2

if __name__ == '__main__':
    rectangle_dimensions = [5, 3]
    circle_dimensions = [4]
    print("Rectangle Area:", calculate_area('rectangle', rectangle_dimensions))
    print("Circle Area:", calculate_area('circle', circle_dimensions))