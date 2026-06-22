import math

def calculate_ellipse_area(a, b):
    return math.pi * a * b

def area_ratio():
    semi_major_a = 5
    semi_minor_b = 3
    semi_major_c = 4
    semi_minor_d = 2
    
    area1 = calculate_ellipse_area(semi_major_a, semi_minor_b)
    area2 = calculate_ellipse_area(semi_major_c, semi_minor_d)
    
    ratio = max(area1, area2) / min(area1, area2)
    return ratio

if __name__ == '__main__':
    print(area_ratio())