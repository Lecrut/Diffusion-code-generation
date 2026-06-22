from math import pi

def ellipse_area(semi_major, semi_minor):
    return pi * semi_major * semi_minor

if __name__ == '__main__':
    axis_a = 4.5
    axis_b = 2.5
    calculated_area = ellipse_area(axis_a, axis_b)
    print(calculated_area)