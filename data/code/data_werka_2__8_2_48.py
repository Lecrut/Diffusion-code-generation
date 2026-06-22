class Polygon:
    def __init__(self, vertices):
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices")
        self.vertices = vertices

    def area(self):
        n = len(self.vertices)
        total_area = 0.0
        for i in range(n):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % n]
            total_area += (x1 * y2 - x2 * y1)
        return abs(total_area) / 2.0

if __name__ == '__main__':
    sample_vertices_1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    polygon1 = Polygon(sample_vertices_1)
    print(polygon1.area())

    sample_vertices_2 = [(1, 1), (4, 5), (7, 1)]
    polygon2 = Polygon(sample_vertices_2)
    print(polygon2.area())