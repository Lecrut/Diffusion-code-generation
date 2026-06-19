import math

class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    def perimeter(self):
        n = len(self.vertices)
        if n < 3:
            raise ValueError("A polygon must have at least three vertices.")
        return sum(Polygon.distance(self.vertices[i], self.vertices[(i + 1) % n]) for i in range(n))

if __name__ == '__main__':
    sample_polygon = Polygon([(0, 0), (4, 0), (4, 3), (0, 3)])
    print(f"Perimeter of the polygon: {sample_polygon.perimeter()}")