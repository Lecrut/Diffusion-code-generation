def calculate_triangle_area(x1, y1, x2, y2):
    return abs((x1 * y2 - x2 * y1)) / 2

if __name__ == '__main__':
    x1, y1 = 3, 4
    x2, y2 = 6, 8
    area = calculate_triangle_area(x1, y1, x2, y2)
    print(area)