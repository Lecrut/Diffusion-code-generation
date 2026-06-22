import math

def calculate_ellipse_area(a, b):
    return math.pi * a * b

def compute_ratio():
    semi_major_a = 5
    semi_minor_b = 3
    area1 = calculate_ellipse_area(semi_major_a, semi_minor_b)
    
    semi_major_c = 4
    semi_minor_d = 2
    area2 = calculate_ellipse_area(semi_major_c, semi_minor_d)
    
    if area1 > area2:
        return area1 / area2
    else:
        return area2 / area1

if __name__ == '__main__':
    ratio = compute_ratio()
    print(ratio)