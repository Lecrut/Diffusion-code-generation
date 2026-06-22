import math

def compute_ellipse_area(semi_major, semi_minor):
    return math.pi * semi_major * semi_minor

if __name__ == '__main__':
    major_axis = 5
    minor_axis = 3
    result = compute_ellipse_area(major_axis, minor_axis)
    print(result)