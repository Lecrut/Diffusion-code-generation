def calculate_triangle_area(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    determinant = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    return abs(determinant) / 2.0
if __name__ == '__main__':
    vertices = [(1, 1), (4, 5), (7, 2)]
    area = calculate_triangle_area(*vertices)
    print(area)