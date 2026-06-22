def calculate_triangle_area(x1, y1):
    return abs(0.5 * x1 * y1)
if __name__ == '__main__':
    x = 3
    y = 4
    area = calculate_triangle_area(x, y)
    print(area)