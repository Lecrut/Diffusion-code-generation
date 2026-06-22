import math

def area_of_ellipse(a, b):
    return math.pi * a * b

def validate_dimensions(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Semi-major and semi-minor axes must be numbers")
    if a <= 0 or b <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive")

if __name__ == '__main__':
    validate_dimensions(3, 2)
    ellipse1_area = area_of_ellipse(3, 2)
    
    validate_dimensions(4, 1)
    ellipse2_area = area_of_ellipse(4, 1)
    
    total_area = ellipse1_area + ellipse2_area
    print(total_area)