def calculate_areas():
    side_length_square = 5
    base_triangle = 4
    height_triangle = 6
    area_square = side_length_square ** 2
    area_triangle = 0.5 * base_triangle * height_triangle
    return area_square > area_triangle

if __name__ == '__main__':
    print(calculate_areas())