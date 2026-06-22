def calculate_polygon_area(vertices):
    if len(vertices) < 3:
        return 0.0
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0

if __name__ == '__main__':
    sample_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    result = calculate_polygon_area(sample_vertices)
    print(result)
    square_vertices = [(0, 0), (5, 0), (5, 5), (0, 5)]
    square_result = calculate_polygon_area(square_vertices)
    print(square_result)
    triangle_vertices = [(0, 0), (3, 0), (1.5, 2.598076211)]
    triangle_result = calculate_polygon_area(triangle_vertices)
    print(triangle_result)