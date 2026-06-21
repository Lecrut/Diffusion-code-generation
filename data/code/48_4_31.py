import math

class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices
        if len(vertices) < 3:
            raise ValueError('A polygon must have at least 3 vertices')

    def distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def perimeter(self):
        total = 0
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            total += self.distance(self.vertices[i], self.vertices[(i + 1) % num_vertices])
        return total

if __name__ == '__main__':
    pentagon_vertices = [(0, 0), (2, 5), (7, 9), (4, 8), (-3, 3)]
    pentagon = Polygon(pentagon_vertices)
    print('Perimeter of the pentagon:', pentagon.perimeter())

    hexagon_vertices = [(1, 1), (4, 1), (6, 5), (4, 9), (1, 9), (-2, 5)]
    hexagon = Polygon(hexagon_vertices)
    print('Perimeter of the hexagon:', hexagon.perimeter())