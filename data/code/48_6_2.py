import math
class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices
    def calculate_perimeter(self):
        perimeter = 0
        n = len(self.vertices)
        for i in range(n):
            p1 = self.vertices[i]
            p2 = self.vertices[(i + 1) % n]
            distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
            perimeter += distance
        return perimeter
if __name__ == '__main__':
    sample_vertices = [
        (0, 0),
        (3, 0),
        (3, 4),
        (0, 4)
    ]
    polygon = Polygon(sample_vertices)
    perimeter = polygon.calculate_perimeter()
    print(perimeter)