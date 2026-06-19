import math

class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    @staticmethod
    def distance(point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def perimeter(self):
        total_distance = 0
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            total_distance += self.distance(self.vertices[i], self.vertices[(i + 1) % num_vertices])
        return total_distance

if __name__ == '__main__':
    sample_polygon = Polygon([(0, 0), (4, 0), (4, 3), (0, 3)])
    print(f"Perimeter of the polygon: {sample_polygon.perimeter()}")