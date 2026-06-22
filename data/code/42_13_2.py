import math

def ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    a = 5.0
    b = 3.0
    print(ellipse_area(a, b))