import math

def compute_ellipse_area():
    semi_major = 5.0
    semi_minor = 3.0
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    print(compute_ellipse_area())