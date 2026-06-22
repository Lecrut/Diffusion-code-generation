import math

def compute_ellipse_area():
    a = 5.0
    b = 3.0
    return math.pi * a * b

if __name__ == '__main__':
    result = compute_ellipse_area()
    print(result)