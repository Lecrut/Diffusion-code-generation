import math

def calculate_ellipse_area(semi_major, semi_minor):
    if not isinstance(semi_major, (int, float)) or not isinstance(semi_minor, (int, float)):
        raise TypeError("Semi-major and semi-minor axes must be numbers.")
    if semi_major <= 0 or semi_minor <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive numbers.")
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    a = 5.0
    b = 3.0
    area = calculate_ellipse_area(a, b)
    print(area)