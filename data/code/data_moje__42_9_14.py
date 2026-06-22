import math

PI_CONSTANT = math.pi

def calculate_ellipse_area(semi_major_axis, semi_minor_axis):
    return PI_CONSTANT * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    axis_a = 4
    axis_b = 2
    computed_area = calculate_ellipse_area(axis_a, axis_b)
    print(computed_area)