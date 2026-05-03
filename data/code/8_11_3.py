import math
def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    area_sum = 0.0
    for i in range(n):
        x_i, y_i = vertices[i]
        x_next, y_next = vertices[(i + 1) % n]
        area_sum += (x_i * y_next - x_next * y_i)
    area = 0.5 * abs(area_sum)
    return area
if __name__ == '__main__':
    polygon1 = [(0, 0), (1, 0), (0, 1)]
    area1 = calculate_polygon_area(polygon1)
    print(f"Area of Polygon 1: {area1}")
    polygon2 = [(2, 1), (4, 5), (7, 3), (5, 0)]
    area2 = calculate_polygon_area(polygon2)
    print(f"Area of Polygon 2: {area2}")
    polygon3 = [(1.5, 2.5), (3.5, 1.5), (2.5, 4.5)]
    area3 = calculate_polygon_area(polygon3)
    print(f"Area of Polygon 3: {area3}")
    polygon4 = [(1.0, 1.0), (1.0, 1.000000000000001), (2.0, 1.0)]
    area4 = calculate_polygon_area(polygon4)
    print(f"Area of Polygon 4 (testing float stability): {area4}")