import math

def validate_axes(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive numbers.")

def ellipse_area(a, b):
    validate_axes(a, b)
    return math.pi * a * b

def area_ratio():
    semi_major_1 = 5
    semi_minor_1 = 3
    semi_major_2 = 4
    semi_minor_2 = 2
    
    area_1 = ellipse_area(semi_major_1, semi_minor_1)
    area_2 = ellipse_area(semi_major_2, semi_minor_2)
    
    if area_1 > area_2:
        return area_1 / area_2
    else:
        return area_2 / area_1

if __name__ == '__main__':
    print(area_ratio())