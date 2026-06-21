def calculate_triangle_area(x1, y1):
    return abs(0.5 * (0 * (y1 - 0) + x1 * (0 - 0) + 0 * (0 - y1)))
if __name__ == '__main__':
    x = 3
    y = 4
    area = calculate_triangle_area(x, y)
    print(area)