import math

def ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    area = ellipse_area(3, 4) + ellipse_area(5, 6)
    print(area)