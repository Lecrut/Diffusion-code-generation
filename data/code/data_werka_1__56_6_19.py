class Polygon:
    def __init__(self, vertices):
        if not isinstance(vertices, list) or len(vertices) < 3:
            raise ValueError("Vertices must be a list of at least three points.")
        for vertex in vertices:
            if not (isinstance(vertex, list) and len(vertex) == 2):
                raise ValueError("Each vertex must be a list of two coordinates.")
        self.vertices = vertices

    def calculate_area(self):
        n = len(self.vertices)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += self.vertices[i][0] * self.vertices[j][1]
            area -= self.vertices[j][0] * self.vertices[i][1]
        return abs(area) / 2.0

if __name__ == '__main__':
    polygon1_vertices = [
        [1, 1],
        [3, 4],
        [7, 3],
        [5, 1]
    ]

    polygon2_vertices = [
        [0, 0],
        [4, 0],
        [4, 3],
        [0, 3]
    ]

    try:
        polygon1 = Polygon(polygon1_vertices)
        print("Area of polygon1:", polygon1.calculate_area())

        polygon2 = Polygon(polygon2_vertices)
        print("Area of polygon2:", polygon2.calculate_area())
    except ValueError as e:
        print(e)