import math

def area_ellipse(a, b):
    return math.pi * a * b

def area_rectangle(w, h):
    return w * h

def check_area_equality():
    ellipse_a = 5
    ellipse_b = 3
    rectangle_w = 10
    rectangle_h = 6
    ellipse_area = area_ellipse(ellipse_a, ellipse_b)
    rectangle_area = area_rectangle(rectangle_w, rectangle_h)
    return math.isclose(ellipse_area, rectangle_area)

if __name__ == '__main__':
    print(check_area_equality())