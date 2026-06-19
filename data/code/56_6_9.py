class Polygon:
    def __init__(self, vertices):
        if not self._validate_vertices(vertices):
            raise ValueError("Invalid vertex coordinates")
        self.vertices = vertices

    def _validate_vertices(self, vertices):
        return isinstance(vertices, list) and len(vertices) >= 3 and all(isinstance(v, tuple) and len(v) == 2 for v in vertices)

    def calculate_area(self):
        if len(self.vertices) < 3:
            return 0.0
        n = len(self.vertices)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += self.vertices[i][0] * self.vertices[j][1]
            area -= self.vertices[j][0] * self.vertices[i][1]
        return abs(area) / 2.0

if __name__ == '__main__':
    polygon1_vertices = [
        [1, 5],
        [3, 8],
        [7, 6],
        [5, 4]
    ]
    polygon2_vertices = [
        [2, 3],
        [6, 9],
        [8, 7]
    ]

    polygon1 = Polygon(polygon1_vertices)
    polygon2 = Polygon(polygon2_vertices)

    print("Area of polygon1:", polygon1.calculate_area())
    print("Area of polygon2:", polygon2.calculate_area())