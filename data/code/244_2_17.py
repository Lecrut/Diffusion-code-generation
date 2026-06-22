import math

def validate_ellipse_dimensions(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive")

def area_of_ellipse(a, b):
    validate_ellipse_dimensions(a, b)
    return math.pi * a * b

if __name__ == '__main__':
    ellipse1_area = area_of_ellipse(3, 2)
    ellipse2_area = area_of_ellipse(4, 1)
    total_area = ellipse1_area + ellipse2_area
    print(total_area)