import math
import numbers

def calculate_ellipse_area(semi_major: float, semi_minor: float) -> float:
    if not isinstance(semi_major, numbers.Real):
        raise TypeError("semi_major must be a real number")
    if not isinstance(semi_minor, numbers.Real):
        raise TypeError("semi_minor must be a real number")
    if semi_major < 0:
        raise ValueError("semi_major must be non-negative")
    if semi_minor < 0:
        raise ValueError("semi_minor must be non-negative")
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    a = 5.0
    b = 3.0
    area = calculate_ellipse_area(a, b)
    print(area)