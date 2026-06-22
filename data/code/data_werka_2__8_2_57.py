class Polygon:
    def __init__(self, vertices):
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices")
        self.vertices = vertices

    @staticmethod
    def _cross_product(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return x1 * y2 - x2 * y1

    def area(self):
        total_area = 0.0
        n = len(self.vertices)
        for i in range(n):
            current_vertex = self.vertices[i]
            next_vertex = self.vertices[(i + 1) % n]
            total_area += Polygon._cross_product(current_vertex, next_vertex)
        return abs(total_area) / 2.0

if __name__ == '__main__':
    sample_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    polygon = Polygon(sample_vertices)
    print(polygon.area())