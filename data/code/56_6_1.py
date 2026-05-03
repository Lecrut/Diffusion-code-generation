class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices
    def calculate_area(self):
        n = len(self.vertices)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += self.vertices[i][0] * self.vertices[j][1]
            area -= self.vertices[j][0] * self.vertices[i][1]
        return abs(area) / 2.0
if __name__ == '__main__':
    polygon1_vertices = [
        [1, 1],
        [3, 4],
        [7, 2],
        [5, 0]
    ]
    polygon2_vertices = [
        [0, 0],
        [5, 0],
        [5, 5],
        [0, 5]
    ]
    poly1 = Polygon(polygon1_vertices)
    poly2 = Polygon(polygon2_vertices)
    area1 = poly1.calculate_area()
    area2 = poly2.calculate_area()
    print(f"Area of Polygon 1: {area1}")
    print(f"Area of Polygon 2: {area2}")