import math

def compute_ellipse_area(semi_major, semi_minor):
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    a = 5
    b = 3
    area = compute_ellipse_area(a, b)
    print(area)