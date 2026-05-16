import math
def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    sum1 = 0.0
    sum2 = 0.0
    for i in range(n):
        x_i, y_i = vertices[i]
        x_next, y_next = vertices[(i + 1) % n]
        sum1 += x_i * y_next
        sum2 += y_i * x_next
    area = 0.5 * (sum1 - sum2)
    if area < 0:
        area = -area
    return area
if __name__ == '__main__':
    sample_vertices_1 = [(0, 0), (1, 0), (0, 1)]
    area_1 = calculate_polygon_area(sample_vertices_1)
    print(f"Area 1: {area_1}")
    sample_vertices_2 = [(2, 1), (4, 5), (7, 3), (5, 0)]
    area_2 = calculate_polygon_area(sample_vertices_2)
    print(f"Area 2: {area_2}")
    sample_vertices_3 = [(1.5, 2.5), (3.5, 1.5), (2.5, 4.5)]
    area_3 = calculate_polygon_area(sample_vertices_3)
    print(f"Area 3: {area_3}")
    sample_vertices_4 = [(0, 0), (10, 0), (10, 10), (0, 10)]
    area_4 = calculate_polygon_area(sample_vertices_4)
    print(f"Area 4: {area_4}")