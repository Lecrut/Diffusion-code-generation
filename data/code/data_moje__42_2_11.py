from math import pi

PI = 3.141592653589793

def calculate_ellipse_area(semi_major, semi_minor):
    return semi_major * semi_minor * PI

def _get_sample_axes():
    return 5.0, 3.0

def _compute_and_display():
    major, minor = _get_sample_axes()
    area = calculate_ellipse_area(major, minor)
    print(area)

if __name__ == '__main__':
    _compute_and_display()