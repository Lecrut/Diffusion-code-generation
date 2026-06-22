import math

def validate_ellipse_axes(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Semi-major and semi-minor axes must be numbers")

def ellipse_area(a, b):
    return math.pi * a * b

def combined_ellipse_areas(a1, b1, a2, b2):
    validate_ellipse_axes(a1, b1)
    validate_ellipse_axes(a2, b2)
    area1 = ellipse_area(a1, b1)
    area2 = ellipse_area(a2, b2)
    return area1 + area2

if __name__ == '__main__':
    total_area = combined_ellipse_areas(3, 4, 5, 6)
    print(total_area)