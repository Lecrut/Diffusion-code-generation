import math

def calculate_ellipse_area(a, b):
    return math.pi * a * b

def compute_area_ratio():
    semi_major_axis1 = 5
    semi_minor_axis1 = 3
    area1 = calculate_ellipse_area(semi_major_axis1, semi_minor_axis1)
    
    semi_major_axis2 = 4
    semi_minor_axis2 = 2
    area2 = calculate_ellipse_area(semi_major_axis2, semi_minor_axis2)
    
    if area1 > area2:
        ratio = area1 / area2
    else:
        ratio = area2 / area1
    
    return ratio

if __name__ == '__main__':
    print(compute_area_ratio())