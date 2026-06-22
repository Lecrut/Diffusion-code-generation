def compare_areas():
    side_length_square = 6
    base_triangle = 4
    height_triangle = 5
    area_square = side_length_square ** 2
    area_triangle = 0.5 * base_triangle * height_triangle
    return area_square > area_triangle

if __name__ == '__main__':
    print(compare_areas())