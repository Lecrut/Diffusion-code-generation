import math

def calculate_ellipse_area(semi_major, semi_minor):
    if not isinstance(semi_major, (int, float)) or not isinstance(semi_minor, (int, float)):
        raise TypeError("Inputs must be numbers")
    if semi_major <= 0 or semi_minor <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive")
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    test_cases = [
        (5, 3),
        (10, 10),
        (1.5, 2.5)
    ]
    for major, minor in test_cases:
        area = calculate_ellipse_area(major, minor)
        print(f"Area with semi-major {major} and semi-minor {minor}: {area}")