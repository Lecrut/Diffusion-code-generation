import math

def _validate_axes(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Axes must be numeric")
    if a <= 0 or b <= 0:
        raise ValueError("Axes must be positive")

def calculate_ellipse_area(semi_major, semi_minor):
    _validate_axes(semi_major, semi_minor)
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    sample_a = 4.0
    sample_b = 2.5
    result = calculate_ellipse_area(sample_a, sample_b)
    print(result)