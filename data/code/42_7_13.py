import math
import numbers

def calculate_ellipse_area(semi_major: float, semi_minor: float) -> float:
    if not isinstance(semi_major, numbers.Real) or not isinstance(semi_minor, numbers.Real):
        raise TypeError("Semi-major and semi-minor axes must be numeric.")
    if semi_major < 0 or semi_minor < 0:
        raise ValueError("Semi-major and semi-minor axes must be non-negative.")
    if semi_major == 0 or semi_minor == 0:
        return 0.0
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    print(calculate_ellipse_area(5.0, 3.0))
    print(calculate_ellipse_area(10.0, 10.0))
    print(calculate_ellipse_area(0.0, 5.0))