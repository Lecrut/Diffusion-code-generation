import math
def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    area_sum = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area_sum += (x1 * y2 - x2 * y1)
    area = 0.5 * abs(area_sum)
    return area
if __name__ == '__main__':
    polygon1 = [(0, 0), (1, 0), (0, 1)]
    area1 = calculate_polygon_area(polygon1)
    print(f"Area of Polygon 1: {area1}")
    polygon2 = [(2, 1), (4, 3), (3, 5), (1, 4)]
    area2 = calculate_polygon_area(polygon2)
    print(f"Area of Polygon 2: {area2}")
    polygon3 = [(1.5, 2.5), (5.0, 1.0), (3.5, 6.0)]
    area3 = calculate_polygon_area(polygon3)
    print(f"Area of Polygon 3: {area3}")
    polygon4 = [(0, 0), (10, 0), (10, 10), (0, 10)]
    area4 = calculate_polygon_area(polygon4)
    print(f"Area of Polygon 4: {area4}")