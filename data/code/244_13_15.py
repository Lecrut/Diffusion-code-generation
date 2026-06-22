import math

def ellipse_area(a, b):
    return math.pi * a * b

def combined_ellipse_areas(a1, b1, a2, b2):
    area1 = ellipse_area(a1, b1)
    area2 = ellipse_area(a2, b2)
    return area1 + area2

if __name__ == '__main__':
    total_area = combined_ellipse_areas(3, 4, 5, 6)
    print(total_area)