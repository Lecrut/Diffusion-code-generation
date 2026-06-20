def triangle_area_shoelace(vertex_a, vertex_b, vertex_c):
    x1, y1 = vertex_a
    x2, y2 = vertex_b
    x3, y3 = vertex_c
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

if __name__ == '__main__':
    point1 = (0, 0)
    point2 = (4, 0)
    point3 = (0, 3)
    area = triangle_area_shoelace(point1, point2, point3)
    print(area)