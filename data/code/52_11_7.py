def calculate_triangle_area(x, y):
    return abs(0.5 * (x * 0 + y * 0 - 0 * y - 0 * x))

if __name__ == '__main__':
    sample_x = 7.0
    sample_y = 24.0
    area = calculate_triangle_area(sample_x, sample_y)
    print(area)