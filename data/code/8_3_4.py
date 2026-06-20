def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0

    sum1 = 0.0
    sum2 = 0.0

    for i in range(n):
        x_curr, y_curr = vertices[i]
        x_next, y_next = vertices[(i + 1) % n]
        sum1 += x_curr * y_next
        sum2 += y_curr * x_next

    return abs(sum1 - sum2) / 2.0

if __name__ == '__main__':
    poly1 = [(0, 0), (4, 0), (4, 4), (0, 4)]
    print(calculate_polygon_area(poly1))

    poly2 = [(0, 0), (5, 0), (2.5, 3)]
    print(calculate_polygon_area(poly2))

    poly3 = [(1, 1), (4, 1), (4, 3), (1, 3), (1, 1)]
    print(calculate_polygon_area(poly3))