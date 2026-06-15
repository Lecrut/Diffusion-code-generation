import math
def polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0
if __name__ == '__main__':
    polygon1_vertices = [
        [0, 0],
        [1, 0],
        [0, 1]
    ]
    polygon2_vertices = [
        [1, 1],
        [3, 1],
        [2, 3]
    ]
    area1 = polygon_area(polygon1_vertices)
    area2 = polygon_area(polygon2_vertices)
    print(f"Area of Polygon 1: {area1}")
    print(f"Area of Polygon 2: {area2}")