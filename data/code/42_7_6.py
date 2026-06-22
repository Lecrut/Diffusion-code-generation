import math

def calculate_ellipse_area(semi_major: float, semi_minor: float) -> float:
    if semi_major <= 0 or semi_minor <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive")
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    major_axis = 5.0
    minor_axis = 3.0
    area = calculate_ellipse_area(major_axis, minor_axis)
    print(area)