import math

def calculate_ellipse_area(semi_major: float, semi_minor: float) -> float:
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    print(calculate_ellipse_area(10.0, 4.0))