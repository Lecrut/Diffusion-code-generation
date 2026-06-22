import math

def calculate_ellipse_area(semi_major: float, semi_minor: float) -> float:
    if semi_major <= 0 or semi_minor <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive numbers.")
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    result = calculate_ellipse_area(5, 3)
    print(result)