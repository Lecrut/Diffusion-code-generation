import math

class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    def perimeter(self):
        if len(self.vertices) < 2:
            return 0.0
        total_distance = 0.0
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % num_vertices]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            total_distance += distance
        return total_distance

if __name__ == '__main__':
    sample_polygon = Polygon([(0, 0), (4, 0), (4, 3), (0, 3)])
    print(f"Perimeter: {sample_polygon.perimeter()}")