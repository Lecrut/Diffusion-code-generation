def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        x_i, y_i = vertices[i]
        x_j, y_j = vertices[j]
        area += x_i * y_j - y_i * x_j
    return abs(area) / 2.0
if __name__ == '__main__':
    polygon_vertices = [(0, 0), (4, 0), (4, 4), (0, 4)]
    area = calculate_polygon_area(polygon_vertices)
    print(area)