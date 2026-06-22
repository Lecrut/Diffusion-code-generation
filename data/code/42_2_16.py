def calculate_ellipse_area(semi_major_axis, semi_minor_axis):
    return 3.141592653589793 * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    a = 5.0
    b = 3.0
    area = calculate_ellipse_area(a, b)
    print(area)