import math

def ellipse_area(a, b):
    return math.pi * a * b

def calculate_ratio():
    semi_major_a = 5
    semi_minor_a = 3
    semi_major_b = 4
    semi_minor_b = 2
    
    area_a = ellipse_area(semi_major_a, semi_minor_a)
    area_b = ellipse_area(semi_major_b, semi_minor_b)
    
    if area_a > area_b:
        larger_area = area_a
        smaller_area = area_b
    else:
        larger_area = area_b
        smaller_area = area_a
    
    ratio = larger_area / smaller_area
    return ratio

if __name__ == '__main__':
    print(calculate_ratio())