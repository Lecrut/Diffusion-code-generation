class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    def calculate_area(self):
        n = len(self.vertices)
        if n < 3:
            return 0.0
        area = sum(self._shoelace_pairwise(i) for i in range(n))
        return abs(area) / 2.0

    def _shoelace_pairwise(self, i):
        j = (i + 1) % len(self.vertices)
        return self.vertices[i][0] * self.vertices[j][1] - self.vertices[j][0] * self.vertices[i][1]

if __name__ == '__main__':
    polygon1_vertices = [
        [2, 3],
        [8, 6],
        [5, 7]
    ]
    polygon2_vertices = [
        [4, 1],
        [9, 2],
        [6, 5],
        [3, 0]
    ]

    polygon1 = Polygon(polygon1_vertices)
    polygon2 = Polygon(polygon2_vertices)

    print(f"Area of polygon1: {polygon1.calculate_area()}")
    print(f"Area of polygon2: {polygon2.calculate_area()}")