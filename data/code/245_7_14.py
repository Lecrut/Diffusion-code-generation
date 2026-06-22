import math

def ellipse_area(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

def rectangle_area(width, height):
    return width * height

def compare_areas(ellipse_semi_major, ellipse_semi_minor, rectangle_width, rectangle_height):
    ellipse = ellipse_area(ellipse_semi_major, ellipse_semi_minor)
    rectangle = rectangle_area(rectangle_width, rectangle_height)
    
    if ellipse > rectangle:
        return "Ellipse is larger"
    elif ellipse < rectangle:
        return "Rectangle is larger"
    else:
        return "Areas are equal"

if __name__ == '__main__':
    print(compare_areas(3, 2, 4, 5))