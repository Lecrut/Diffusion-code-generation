class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    def calculate_area(self):
        if not self._is_valid_polygon():
            return 0.0
        return abs(self._shoelace_formula()) / 2.0

    def _is_valid_polygon(self):
        return len(self.vertices) >= 3

    def _shoelace_formula(self):
        n = len(self.vertices)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += self.vertices[i][0] * self.vertices[j][1]
            area -= self.vertices[j][0] * self.vertices[i][1]
        return area

if __name__ == '__main__':
    polygon1_vertices = [
        [2, 3],
        [5, 7],
        [8, 4]
    ]
    polygon2_vertices = [
        [1, 1],
        [4, 5],
        [7, 9],
        [10, 5]
    ]

    polygon1 = Polygon(polygon1_vertices)
    polygon2 = Polygon(polygon2_vertices)

    print("Area of Polygon 1:", polygon1.calculate_area())
    print("Area of Polygon 2:", polygon2.calculate_area())