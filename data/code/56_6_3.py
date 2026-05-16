import math
class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices
    def calculate_area(self):
        n = len(self.vertices)
        if n < 3:
            return 0.0
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += (self.vertices[i][0] * self.vertices[j][1] - self.vertices[j][0] * self.vertices[i][1])
        return abs(area) / 2.0
if __name__ == '__main__':
    polygon1_vertices = [
        (1, 6),
        (3, 1),
        (7, 2),
        (4, 8)
    ]
    polygon2_vertices = [
        (0, 0),
        (5, 0),
        (5, 5),
        (0, 5)
    ]
    polygon1 = Polygon(polygon1_vertices)
    polygon2 = Polygon(polygon2_vertices)
    area1 = polygon1.calculate_area()
    area2 = polygon2.calculate_area()
    print(f"Area of Polygon 1: {area1}")
    print(f"Area of Polygon 2: {area2}")