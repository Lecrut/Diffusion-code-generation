def calculate_polygon_area(vertices):
    if len(vertices) < 3:
        return 0.0
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

if __name__ == '__main__':
    square_vertices = [(0, 0), (4, 0), (4, 4), (0, 4)]
    print(calculate_polygon_area(square_vertices))
    triangle_vertices = [(0, 0), (5, 0), (2.5, 3)]
    print(calculate_polygon_area(triangle_vertices))
    pentagon_vertices = [(1, 0), (3.05, 2.245), (0.225, 3.59), (-2.225, 3.59), (-2.225, -0.59)]
    print(calculate_polygon_area(pentagon_vertices))