def calculate_polygon_area(vertices):
    if len(vertices) < 3:
        return 0.0
    area = 0.0
    n = len(vertices)
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

if __name__ == '__main__':
    sample_vertices = [(0, 0), (4, 0), (4, 4), (0, 4)]
    result = calculate_polygon_area(sample_vertices)
    print(result)
    sample_vertices_2 = [(1, 1), (5, 1), (5, 4), (2, 4)]
    result_2 = calculate_polygon_area(sample_vertices_2)
    print(result_2)
    sample_triangle = [(0, 0), (6, 0), (3, 5)]
    result_3 = calculate_polygon_area(sample_triangle)
    print(result_3)