import math

PI = math.pi
A1 = 3
B1 = 4
A2 = 5
B2 = 6

def ellipse_area(a, b):
    return PI * a * b

def combined_ellipse_areas():
    area1 = ellipse_area(A1, B1)
    area2 = ellipse_area(A2, B2)
    return area1 + area2

if __name__ == '__main__':
    total_area = combined_ellipse_areas()
    print(total_area)