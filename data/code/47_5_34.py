def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

if __name__ == '__main__':
    coordinates = {
        'A': (0, 0),
        'B': (4, 0),
        'C': (2, 3)
    }
    area = calculate_triangle_area(*coordinates['A'], *coordinates['B'], *coordinates['C'])
    print(area)