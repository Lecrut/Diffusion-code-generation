import math

def calculate_ellipse_area(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both axes must be numbers")
    if a <= 0 or b <= 0:
        raise ValueError("Both axes must be positive numbers")
    return math.pi * a * b

if __name__ == '__main__':
    print(calculate_ellipse_area(5, 3))
    print(calculate_ellipse_area(10, 10))
    print(calculate_ellipse_area(1, 2))