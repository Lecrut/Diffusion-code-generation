import math

def calculate_ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    semi_major = 5.0
    semi_minor = 3.0
    area = calculate_ellipse_area(semi_major, semi_minor)
    print(area)