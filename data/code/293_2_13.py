import math

def calculate_area(shape_type, *params):
    if shape_type == 'circle':
        radius = params[0]
        return math.pi * radius ** 2
    elif shape_type == 'square':
        side = params[0]
        return side ** 2
    elif shape_type == 'rectangle':
        length, width = params
        return length * width
    else:
        raise ValueError('Unsupported shape type')
if __name__ == '__main__':
    print(calculate_area('circle', 5))
    print(calculate_area('square', 4))
    print(calculate_area('rectangle', 3, 2))