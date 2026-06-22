import math

def ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    semi_major = 5
    semi_minor = 3
    area = ellipse_area(semi_major, semi_minor)
    print(area)