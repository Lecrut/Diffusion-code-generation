def compare_areas():
    side_square = 5
    base_triangle = 4
    height_triangle = 6

    area_square = side_square ** 2
    area_triangle = (base_triangle * height_triangle) / 2

    return area_square > area_triangle

if __name__ == '__main__':
    print(compare_areas())