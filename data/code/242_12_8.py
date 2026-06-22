import math

def calculate_ellipse_area(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

def compute_area_ratio():
    semi_major_a = 6
    semi_minor_a = 4
    semi_major_b = 5
    semi_minor_b = 3
    
    area_a = calculate_ellipse_area(semi_major_a, semi_minor_a)
    area_b = calculate_ellipse_area(semi_major_b, semi_minor_b)
    
    if area_a > area_b:
        larger_area = area_a
        smaller_area = area_b
    else:
        larger_area = area_b
        smaller_area = area_a
    
    ratio = larger_area / smaller_area
    return ratio

if __name__ == '__main__':
    print(compute_area_ratio())