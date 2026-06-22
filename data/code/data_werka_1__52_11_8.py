def calculate_triangle_area(x, y):
    return abs(0.5 * x * y)

if __name__ == '__main__':
    sample_x = 7
    sample_y = 24
    area = calculate_triangle_area(sample_x, sample_y)
    print(area)