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
    return area
if __name__ == '__main__':
    sample_vertices1 = [(0, 0), (1, 0), (0, 1)]
    area1 = calculate_polygon_area(sample_vertices1)
    print(f"Area 1: {area1}")
    sample_vertices2 = [(2, 1), (4, 5), (7, 3), (5, 0)]
    area2 = calculate_polygon_area(sample_vertices2)
    print(f"Area 2: {area2}")
    sample_vertices3 = [(1.5, 2.5), (3.0, 1.0), (0.5, 4.0)]
    area3 = calculate_polygon_area(sample_vertices3)
    print(f"Area 3: {area3}")
    sample_vertices4 = [(1.0, 1.0), (1.0, 1.000000000000001), (2.0, 1.0)]
    area4 = calculate_polygon_area(sample_vertices4)
    print(f"Area 4 (Testing float tolerance): {area4}")