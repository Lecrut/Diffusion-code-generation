import math

def ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    area1 = ellipse_area(3, 2)
    area2 = ellipse_area(4, 1)
    total_area = area1 + area2
    print(total_area)