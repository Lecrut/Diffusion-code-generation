import math

def validate_parameters(expected_count, args, shape_name):
    if len(args) != expected_count:
        raise ValueError(f'{shape_name} requires {expected_count} parameter(s).')

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_area(shape_type, *args):
    if shape_type == 'rectangle':
        validate_parameters(2, args, 'Rectangle')
        width, height = args
        return calculate_rectangle_area(width, height)
    elif shape_type == 'circle':
        validate_parameters(1, args, 'Circle')
        radius = args[0]
        return calculate_circle_area(radius)
    elif shape_type == 'triangle':
        validate_parameters(2, args, 'Triangle')
        base, height = args
        return calculate_triangle_area(base, height)
    else:
        raise ValueError(f'Unsupported shape type: {shape_type}')
if __name__ == '__main__':
    print(calculate_area('rectangle', 5, 10))
    print(calculate_area('circle', 7))
    print(calculate_area('triangle', 8, 6))