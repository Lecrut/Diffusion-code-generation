import math

def calculate_ellipse_area(semi_major, semi_minor):
    if not isinstance(semi_major, (int, float)) or not isinstance(semi_minor, (int, float)):
        raise TypeError("Inputs must be numbers.")
    if semi_major <= 0 or semi_minor <= 0:
        raise ValueError("Inputs must be positive numbers.")
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    print(calculate_ellipse_area(5, 3))
    print(calculate_ellipse_area(10, 2.5))
    print(calculate_ellipse_area(1, 1))