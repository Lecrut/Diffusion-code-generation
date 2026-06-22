import math

def calculate_area(shape_type, dimensions):
    if shape_type.lower() == 'circle':
        return _calculate_circle_area(dimensions[0])
    elif shape_type.lower() == 'rectangle':
        return _calculate_rectangle_area(dimensions)
    else:
        raise ValueError('Unsupported shape type')

def _calculate_circle_area(radius):
    return math.pi * radius ** 2

def _calculate_rectangle_area(dimensions):
    length, width = dimensions
    return length * width
if __name__ == '__main__':
    print(calculate_area('circle', [5]))
    print(calculate_area('rectangle', [4, 6]))