import math

def compute_ellipse_area(semi_major, semi_minor):
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    a = 5.0
    b = 3.0
    result = compute_ellipse_area(a, b)
    print(result)