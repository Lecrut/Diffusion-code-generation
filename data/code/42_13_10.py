import math

def _validate_dimensions(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Semi-axes must be numeric.")
    if a <= 0 or b <= 0:
        raise ValueError("Semi-axes must be positive numbers.")

def calculate_ellipse_area(a, b):
    _validate_dimensions(a, b)
    return math.pi * a * b

if __name__ == '__main__':
    SEMI_MAJOR = 10.0
    SEMI_MINOR = 4.5
    result = calculate_ellipse_area(SEMI_MAJOR, SEMI_MINOR)
    print(result)