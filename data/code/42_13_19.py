import math

PI_CONSTANT = math.pi

def calculate_ellipse_area(semi_major, semi_minor):
    return PI_CONSTANT * semi_major * semi_minor

if __name__ == '__main__':
    axis_a = 7.5
    axis_b = 4.2
    computed_area = calculate_ellipse_area(axis_a, axis_b)
    print(computed_area)