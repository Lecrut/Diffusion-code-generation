import math
import functools

def calculate_ellipse_area(semi_major_axis, semi_minor_axis):
    return functools.reduce(lambda x, y: x * y, [math.pi, semi_major_axis, semi_minor_axis])

if __name__ == '__main__':
    axis_a = 10
    axis_b = 4
    computed_area = calculate_ellipse_area(axis_a, axis_b)
    print(computed_area)