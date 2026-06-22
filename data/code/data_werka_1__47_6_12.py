def calculate_area(x1, y1, x2, y2, x3, y3):
    determinant = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    area = abs(determinant) / 2.0
    return area
if __name__ == '__main__':
    vertex_a = (1, 1)
    vertex_b = (4, 5)
    vertex_c = (7, 2)
    x1, y1 = vertex_a
    x2, y2 = vertex_b
    x3, y3 = vertex_c
    area = calculate_area(x1, y1, x2, y2, x3, y3)
    print(area)