import math
PI = math.pi

def ellipse_area(a, b):
    return PI * a * b

def combined_ellipse_areas(axes1, axes2):
    area1 = ellipse_area(*axes1)
    area2 = ellipse_area(*axes2)
    return area1 + area2
if __name__ == '__main__':
    ellipse1_axes = (3, 4)
    ellipse2_axes = (5, 6)
    total_area = combined_ellipse_areas(ellipse1_axes, ellipse2_axes)
    print(total_area)