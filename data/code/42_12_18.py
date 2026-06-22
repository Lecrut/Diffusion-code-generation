import math

def calculate_ellipse_area(semi_major, semi_minor):
    if not isinstance(semi_major, (int, float)) or not isinstance(semi_minor, (int, float)):
        raise TypeError("Both axes must be numbers")
    if semi_major <= 0 or semi_minor <= 0:
        raise ValueError("Both axes must be positive numbers")
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    test_cases = [(5, 3), (10.5, 2.4), (1, 1), (-2, 5)]
    for major, minor in test_cases:
        try:
            area = calculate_ellipse_area(major, minor)
            print(f"Area for axes {major} and {minor}: {area}")
        except (ValueError, TypeError) as e:
            print(f"Error for axes {major} and {minor}: {e}")