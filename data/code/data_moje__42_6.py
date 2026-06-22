import math

def compute_ellipse_area(semi_major_axis, semi_minor_axis):
    area = math.pi * semi_major_axis * semi_minor_axis
    return area

if __name__ == '__main__':
    a = 5
    b = 3
    result = compute_ellipse_area(a, b)
    print(result)