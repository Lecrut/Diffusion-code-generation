import math

def compute_ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    a = 3
    b = 5
    area = compute_ellipse_area(a, b)
    print(area)