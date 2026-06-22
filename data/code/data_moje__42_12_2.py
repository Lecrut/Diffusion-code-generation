import math

def calculate_ellipse_area(semi_major, semi_minor):
    if not isinstance(semi_major, (int, float)) or not isinstance(semi_minor, (int, float)):
        raise ValueError("Inputs must be numbers")
    if semi_major <= 0 or semi_minor <= 0:
        raise ValueError("Inputs must be positive numbers")
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    test_cases = [
        (5, 3),
        (10, 2),
        (1.5, 1.5)
    ]
    for a, b in test_cases:
        result = calculate_ellipse_area(a, b)
        print(result)