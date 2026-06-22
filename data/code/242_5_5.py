import math
ELLIPSE_SEMI_MAJOR_AXIS = 5
ELLIPSE_SEMI_MINOR_AXIS = 3
TRIANGLE_BASE = 10
TRIANGLE_HEIGHT = 4

def calculate_area_ellipse(semi_major_axis, semi_minor_axis):
    return math.pi * semi_major_axis * semi_minor_axis

def calculate_area_triangle(base, height):
    return 0.5 * base * height
if __name__ == '__main__':
    ellipse_area = calculate_area_ellipse(ELLIPSE_SEMI_MAJOR_AXIS, ELLIPSE_SEMI_MINOR_AXIS)
    triangle_area = calculate_area_triangle(TRIANGLE_BASE, TRIANGLE_HEIGHT)
    print(f'Ellipse area: {ellipse_area}')
    print(f'Triangle area: {triangle_area}')