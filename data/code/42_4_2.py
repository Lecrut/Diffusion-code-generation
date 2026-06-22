def compute_ellipse_area(a, b):
    import math
    return math.pi * a * b

if __name__ == '__main__':
    semi_major = 5.0
    semi_minor = 3.0
    print(compute_ellipse_area(semi_major, semi_minor))