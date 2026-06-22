import math

def calculate_ellipse_area(semi_major, semi_minor):
    return math.pi * semi_major * semi_minor

def _validate_axes(semi_major, semi_minor):
    if semi_major <= 0:
        raise ValueError("semi-major axis must be positive")
    if semi_minor <= 0:
        raise ValueError("semi-minor axis must be positive")

if __name__ == '__main__':
    _validate_axes(10, 6)
    result = calculate_ellipse_area(10, 6)
    print(result)