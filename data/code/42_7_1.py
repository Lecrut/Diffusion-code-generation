import math

def calculate_ellipse_area(a: float, b: float) -> float:
    if a <= 0 or b <= 0:
        raise ValueError("Semi-axes must be positive.")
    return math.pi * a * b

if __name__ == '__main__':
    semi_major = 5.0
    semi_minor = 3.0
    area = calculate_ellipse_area(semi_major, semi_minor)
    print(area)