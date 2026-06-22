import math

def calculate_ellipse_area(semi_major, semi_minor):
    if semi_major <= 0 or semi_minor <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive numbers.")
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    test_cases = [(5, 3), (10, 2.5), (0, 4), (-2, 5)]
    for major, minor in test_cases:
        try:
            area = calculate_ellipse_area(major, minor)
            print(area)
        except ValueError as e:
            print(e)