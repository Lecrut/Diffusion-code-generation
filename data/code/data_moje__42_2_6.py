def calculate_ellipse_area(semi_major_axis, semi_minor_axis):
    return 3.141592653589793 * semi_major_axis * semi_minor_axis

if __name__ == '__main__':
    result = calculate_ellipse_area(5, 3)
    print(result)