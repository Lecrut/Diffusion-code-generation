import math

def compare_areas(semi_major_axis, semi_minor_axis, width, height):
    ellipse_area = math.pi * semi_major_axis * semi_minor_axis
    rectangle_area = width * height
    return ellipse_area, rectangle_area, ellipse_area > rectangle_area

if __name__ == '__main__':
    print(compare_areas(3, 2, 6, 4))