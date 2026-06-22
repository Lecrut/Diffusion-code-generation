import math

def compute_ellipse_area(a, b):
    return math.pi * a * b

if __name__ == '__main__':
    result = compute_ellipse_area(3.0, 5.0)
    print(result)