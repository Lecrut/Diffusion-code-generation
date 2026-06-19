import math

SHAPE_FORMULAS = {
    'circle': {'circumference': lambda r: 2 * math.pi * r},
    'square': {'perimeter': lambda s: 4 * s}
}

def calculate_shapes(radius, side_length):
    circle_circumference = SHAPE_FORMULAS['circle']['circumference'](radius)
    square_perimeter = SHAPE_FORMULAS['square']['perimeter'](side_length)
    return (circle_circumference, square_perimeter)

if __name__ == '__main__':
    sample_radius = 6.0
    sample_side_length = 8.0
    result = calculate_shapes(sample_radius, sample_side_length)
    print(result)