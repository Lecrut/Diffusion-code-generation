import math

def compute_ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    a_value = 5
    b_value = 3
    area = compute_ellipse_area(a_value, b_value)
    print(area)