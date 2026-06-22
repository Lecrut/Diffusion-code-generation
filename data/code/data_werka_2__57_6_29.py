import math

def calculate_area(shape, dimensions):
    if shape == 'rectangle':
        if len(dimensions) != 2:
            raise ValueError('Rectangle requires exactly two dimensions')
        length, width = dimensions
        return length * width
    elif shape == 'circle':
        if len(dimensions) != 1:
            raise ValueError('Circle requires exactly one dimension (radius)')
        radius = dimensions[0]
        return math.pi * radius ** 2
    elif shape == 'triangle':
        if len(dimensions) != 2:
            raise ValueError('Triangle requires exactly two dimensions (base and height)')
        base, height = dimensions
        return 0.5 * base * height
    else:
        raise ValueError(f'Unsupported shape: {shape}')

if __name__ == '__main__':
    rectangle_dimensions = [5, 3]
    circle_dimensions = [4]
    triangle_dimensions = [8, 4]

    rectangle_area = calculate_area('rectangle', rectangle_dimensions)
    circle_area = calculate_area('circle', circle_dimensions)
    triangle_area = calculate_area('triangle', triangle_dimensions)

    print("Rectangle Area:", rectangle_area)
    print("Circle Area:", circle_area)
    print("Triangle Area:", triangle_area)