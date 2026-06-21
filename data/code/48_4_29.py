import math

class Polygon:
    def __init__(self, vertices):
        if len(vertices) < 3:
            raise ValueError('A polygon must have at least 3 vertices')
        self.vertices = vertices

    def calculate_distance(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def perimeter(self):
        total_perimeter = 0.0
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            distance = self.calculate_distance(self.vertices[i], self.vertices[(i + 1) % num_vertices])
            total_perimeter += distance
        return total_perimeter

if __name__ == '__main__':
    triangle_vertices = [(0, 0), (4, 0), (2, 3)]
    triangle = Polygon(triangle_vertices)
    print('Perimeter of the triangle:', triangle.perimeter())

    quadrilateral_vertices = [(1, 1), (5, 1), (5, 5), (1, 5)]
    quadrilateral = Polygon(quadrilateral_vertices)
    print('Perimeter of the quadrilateral:', quadrilateral.perimeter())