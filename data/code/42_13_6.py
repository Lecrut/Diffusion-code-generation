import math

def ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    a = 5.0
    b = 3.0
    area = ellipse_area(a, b)
    print(area)