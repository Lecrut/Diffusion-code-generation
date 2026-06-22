def calculate_triangle_area(x1, y1):
    return abs(0.5 * (x1 * 0 + y1 * 0 - 0 * y1 - 0 * x1))

if __name__ == '__main__':
    ORIGIN_X = 0
    ORIGIN_Y = 0

    sample_x = 6.0
    sample_y = 8.0

    area = calculate_triangle_area(sample_x, sample_y)
    print(area)