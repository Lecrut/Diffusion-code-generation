import math

class Polygon:

    def __init__(self, vertices):
        self.vertices = vertices

    def distance(self, p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    def perimeter(self):
        total = 0
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            total += self.distance(self.vertices[i], self.vertices[(i + 1) % num_vertices])
        return total
if __name__ == '__main__':
    sample_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    polygon = Polygon(sample_vertices)
    print(polygon.perimeter())