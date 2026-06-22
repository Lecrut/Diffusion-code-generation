def calculate_area(shape, dimensions):
    if shape == 'rectangle':
        if len(dimensions) != 2:
            raise ValueError('Rectangle requires exactly two dimensions')
        length, width = dimensions
        return length * width
    elif shape == 'circle':
        import math
        if len(dimensions) != 1:
            raise ValueError('Circle requires exactly one dimension (radius)')
        radius = dimensions[0]
        return math.pi * radius ** 2
    else:
        raise ValueError(f'Unsupported shape: {shape}')
if __name__ == '__main__':
    rectangle_dimensions = [5, 3]
    circle_dimensions = [4]
    rectangle_area = calculate_area('rectangle', rectangle_dimensions)
    circle_area = calculate_area('circle', circle_dimensions)
    print(f'Rectangle area: {rectangle_area}')
    print(f'Circle area: {circle_area}')