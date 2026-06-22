import math

def calculate_ellipse_area(a, b):
    return math.pi * a * b

def sum_of_areas(area1, area2):
    return area1 + area2

if __name__ == '__main__':
    ellipse_a_area = calculate_ellipse_area(3, 2)
    ellipse_b_area = calculate_ellipse_area(4, 1)
    total_area = sum_of_areas(ellipse_a_area, ellipse_b_area)
    print(total_area)