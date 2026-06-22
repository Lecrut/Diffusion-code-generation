import math

def ellipse_area(a, b):
    return math.pi * a * b

def combined_ellipse_areas(axes1, axes2):
    area1 = ellipse_area(axes1[0], axes1[1])
    area2 = ellipse_area(axes2[0], axes2[1])
    return area1 + area2

if __name__ == '__main__':
    axes_set1 = (3, 4)
    axes_set2 = (5, 6)
    total_area = combined_ellipse_areas(axes_set1, axes_set2)
    print(total_area)