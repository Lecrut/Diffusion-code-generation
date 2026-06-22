import math

def _pi_constant():
    return math.pi

def calculate_ellipse_area(semi_major, semi_minor):
    return _pi_constant() * semi_major * semi_minor

if __name__ == '__main__':
    axis_a = 7.0
    axis_b = 3.5
    result = calculate_ellipse_area(axis_a, axis_b)
    print(result)