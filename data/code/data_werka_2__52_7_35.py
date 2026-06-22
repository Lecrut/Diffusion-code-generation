def calculate_area(x, y):
    return abs(0.5 * (x * 0 + y * 0 - 0 * y - 0 * x))

if __name__ == '__main__':
    sample_x = 6
    sample_y = 8
    area = calculate_area(sample_x, sample_y)
    print(area)