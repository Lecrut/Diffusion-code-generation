import math

def area_of_ellipse(a, b):
    return math.pi * a * b

def sum_of_areas(axes_a, axes_b):
    ellipse1_area = area_of_ellipse(*axes_a)
    ellipse2_area = area_of_ellipse(*axes_b)
    return ellipse1_area + ellipse2_area

if __name__ == '__main__':
    axes_a = (3, 2)
    axes_b = (4, 1)
    total_area = sum_of_areas(axes_a, axes_b)
    print(total_area)