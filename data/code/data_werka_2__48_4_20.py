import math

class Polygon:

    def __init__(self, vertices):
        self.vertices = vertices

    def distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def perimeter(self):
        if len(self.vertices) < 3:
            raise ValueError('A polygon must have at least 3 vertices')
        total = 0
        for i in range(len(self.vertices)):
            total += self.distance(self.vertices[i], self.vertices[(i + 1) % len(self.vertices)])
        return total
if __name__ == '__main__':
    triangle_vertices = [(0, 0), (4, 0), (2, 3)]
    triangle = Polygon(triangle_vertices)
    print('Perimeter of the triangle:', triangle.perimeter())
    quadrilateral_vertices = [(0, 0), (5, 0), (5, 5), (0, 5)]
    quadrilateral = Polygon(quadrilateral_vertices)
    print('Perimeter of the quadrilateral:', quadrilateral.perimeter())