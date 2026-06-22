def polygon_area(vertices):
    n = len(vertices)
    total_area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        cross_product = x1 * y2 - y1 * x2
        total_area += cross_product
    return abs(total_area) / 2.0

if __name__ == '__main__':
    sample_vertices = [(1, 1), (4, 5), (7, 1)]
    area_result = polygon_area(sample_vertices)
    print(area_result)