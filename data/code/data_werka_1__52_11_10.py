def calculate_triangle_area(x, y):
    ORIGIN_X = 0
    ORIGIN_Y = 0
    return abs(0.5 * (x * ORIGIN_Y + y * ORIGIN_X - ORIGIN_Y * x - ORIGIN_X * y))

if __name__ == '__main__':
    SAMPLE_X = 6
    SAMPLE_Y = 8
    area = calculate_triangle_area(SAMPLE_X, SAMPLE_Y)
    print(area)