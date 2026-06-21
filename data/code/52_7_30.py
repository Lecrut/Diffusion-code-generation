def calculate_area(x, y):
    return abs(0.5 * x * y)

if __name__ == '__main__':
    sample_x = 3
    sample_y = 4
    area = calculate_area(sample_x, sample_y)
    print(area)