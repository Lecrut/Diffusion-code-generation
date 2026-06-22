import math

def calculate_ellipse_area(major_axis, minor_axis):
    a = _convert_to_radius(major_axis)
    b = _convert_to_radius(minor_axis)
    _validate_positive(a)
    _validate_positive(b)
    return math.pi * a * b

def _convert_to_radius(axis_length):
    return axis_length / 2

def _validate_positive(value):
    if value <= 0:
        raise ValueError("Dimensions must be positive")

if __name__ == '__main__':
    major_dim = 12
    minor_dim = 8
    computed_area = calculate_ellipse_area(major_dim, minor_dim)
    print(computed_area)