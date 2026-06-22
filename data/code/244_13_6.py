import math

def ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    semi_major1 = 7
    semi_minor1 = 8
    semi_major2 = 9
    semi_minor2 = 10
    area1 = ellipse_area(semi_major1, semi_minor1)
    area2 = ellipse_area(semi_major2, semi_minor2)
    total_area = area1 + area2
    print(total_area)