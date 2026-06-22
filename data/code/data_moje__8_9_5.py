def calculate_polygon_area(vertices):
    if not vertices or len(vertices) < 3:
        return 0.0
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2
        area -= x2 * y1
    area = abs(area) / 2.0
    return round(area, 10)

if __name__ == '__main__':
    sample_vertices = [(0, 0), (4, 0), (4, 4), (0, 4)]
    result = calculate_polygon_area(sample_vertices)
    print(result)