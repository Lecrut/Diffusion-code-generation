import math

class Polygon:
    def __init__(self, vertices):
        if len(vertices) < 3:
            raise ValueError('A polygon must have at least 3 vertices')
        self.vertices = vertices

    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    def perimeter(self):
        total_distance = 0.0
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            total_distance += self.distance(self.vertices[i], self.vertices[(i + 1) % num_vertices])
        return total_distance

if __name__ == '__main__':
    pentagon_vertices = [(0, 0), (4, 0), (6, 3), (3, 7), (-1, 5)]
    pentagon = Polygon(pentagon_vertices)
    print('Perimeter of the pentagon:', pentagon.perimeter())

    square_vertices = [(0, 0), (2, 0), (2, 2), (0, 2)]
    square = Polygon(square_vertices)
    print('Perimeter of the square:', square.perimeter())