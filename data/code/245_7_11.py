import math

def ellipse_area(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

def rectangle_area(length, width):
    return length * width

def compare_areas(ellipse_semi_major, ellipse_semi_minor, rect_length, rect_width):
    ellipse_a = ellipse_area(ellipse_semi_major, ellipse_semi_minor)
    rect_a = rectangle_area(rect_length, rect_width)
    if ellipse_a > rect_a:
        return "Ellipse is larger"
    elif ellipse_a < rect_a:
        return "Rectangle is larger"
    else:
        return "Areas are equal"

if __name__ == '__main__':
    print(compare_areas(5, 3, 10, 4))