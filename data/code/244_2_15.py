import math

def calculate_ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    semi_major_axis1 = 3
    semi_minor_axis1 = 2
    ellipse1_area = calculate_ellipse_area(semi_major_axis1, semi_minor_axis1)
    
    semi_major_axis2 = 4
    semi_minor_axis2 = 1
    ellipse2_area = calculate_ellipse_area(semi_major_axis2, semi_minor_axis2)
    
    total_area = ellipse1_area + ellipse2_area
    print(total_area)