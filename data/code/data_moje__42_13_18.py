import math

def ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    print(ellipse_area(5.0, 3.0))
    print(ellipse_area(10.0, 10.0))
    print(ellipse_area(7.5, 2.2))