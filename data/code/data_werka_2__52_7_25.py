def calculate_triangle_area(x, y):
    return abs(0.5 * (0 * (y - 0) + x * (0 - 0) + 0 * (0 - y)))

if __name__ == '__main__':
    sample_x = 3
    sample_y = 4
    area = calculate_triangle_area(sample_x, sample_y)
    print(area)