import math

class Polygon:

    def __init__(self, vertices):
        self.vertices = vertices

    def perimeter(self):
        if len(self.vertices) < 3:
            raise ValueError('A polygon must have at least 3 vertices.')
        perimeter = 0
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % num_vertices]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            perimeter += distance
        return perimeter
if __name__ == '__main__':
    triangle_vertices = [(0, 0), (3, 0), (3, 4)]
    triangle = Polygon(triangle_vertices)
    print('Perimeter of the triangle:', triangle.perimeter())
    quadrilateral_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    quadrilateral = Polygon(quadrilateral_vertices)
    print('Perimeter of the quadrilateral:', quadrilateral.perimeter())