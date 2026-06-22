import math

def compare_areas(semi_major_axis, semi_minor_axis, width, height):
    ellipse_area = math.pi * semi_major_axis * semi_minor_axis
    rectangle_area = width * height
    return ellipse_area, rectangle_area, ellipse_area > rectangle_area

if __name__ == '__main__':
    semi_major_axis = 5
    semi_minor_axis = 3
    width = 10
    height = 6
    ellipse_area, rectangle_area, is_larger = compare_areas(semi_major_axis, semi_minor_axis, width, height)
    print(f"Ellipse area: {ellipse_area}")
    print(f"Rectangle area: {rectangle_area}")
    print(f"Is the ellipse area larger? {'Yes' if is_larger else 'No'}")