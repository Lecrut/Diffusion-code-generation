import math

class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    def distance_between_vertices(self, v1, v2):
        return math.sqrt((v2[0] - v1[0]) ** 2 + (v2[1] - v1[1]) ** 2)

    def calculate_perimeter(self):
        num_vertices = len(self.vertices)
        if num_vertices < 3:
            raise ValueError('A polygon must have at least 3 vertices.')
        perimeter = 0.0
        for i in range(num_vertices):
            current_vertex = self.vertices[i]
            next_vertex = self.vertices[(i + 1) % num_vertices]
            segment_length = self.distance_between_vertices(current_vertex, next_vertex)
            perimeter += segment_length
        return perimeter

if __name__ == '__main__':
    pentagon_vertices = [(0, 0), (4, 0), (5, 3), (2, 5), (-1, 2)]
    pentagon = Polygon(pentagon_vertices)
    print('Perimeter of the pentagon:', pentagon.calculate_perimeter())