import math

def calculate_ellipse_area(semi_major, semi_minor):
    if semi_major <= 0:
        raise ValueError("Semi-major axis must be a positive number")
    if semi_minor <= 0:
        raise ValueError("Semi-minor axis must be a positive number")
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    print(calculate_ellipse_area(5.0, 3.0))
    print(calculate_ellipse_area(10.5, 2.5))