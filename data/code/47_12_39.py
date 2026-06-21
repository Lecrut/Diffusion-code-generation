class Triangle:
    def __init__(self, p1, p2, p3):
        self.vertices = [p1, p2, p3]

    @staticmethod
    def _validate_vertex(vertex):
        if not isinstance(vertex, tuple) or len(vertex) != 2:
            raise ValueError("Each vertex must be a tuple of two numbers.")
        if not all(isinstance(coord, (int, float)) for coord in vertex):
            raise ValueError("All coordinates must be integers or floats.")

    @classmethod
    def from_vertices(cls, p1, p2, p3):
        cls._validate_vertex(p1)
        cls._validate_vertex(p2)
        cls._validate_vertex(p3)
        return cls(p1, p2, p3)

    def area(self):
        x1, y1 = self.vertices[0]
        x2, y2 = self.vertices[1]
        x3, y3 = self.vertices[2]
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

if __name__ == '__main__':
    vertices = [(0, 0), (4, 0), (2, 3)]
    triangle = Triangle.from_vertices(*vertices)
    area = triangle.area()
    print(area)