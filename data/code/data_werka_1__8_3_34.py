def calculate_polygon_area(vertices):
    num_vertices = len(vertices)
    total_area = 0.0
    for i in range(num_vertices):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % num_vertices]
        cross_product = x1 * y2 - x2 * y1
        total_area += cross_product
    return abs(total_area) / 2.0

if __name__ == '__main__':
    sample_polygon = [(1, 2), (4, 5), (7, 8)]
    area_result = calculate_polygon_area(sample_polygon)
    print(area_result)