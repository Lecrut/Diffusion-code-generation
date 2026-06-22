import math

def calculate_ellipse_area(semi_major, semi_minor):
    if semi_major <= 0 or semi_minor <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive numbers.")
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    test_cases = [
        (5, 3),
        (10, 10),
        (1, 1),
        (7.5, 2.5)
    ]

    for a, b in test_cases:
        result = calculate_ellipse_area(a, b)
        print(result)