class Polygon:
    def __init__(self, vertices):
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices.")
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
        [1, 3],
        [4, 6],
        [7, 5]
    ]
    polygon2_vertices = [
        [2, 1],
        [5, 3],
        [8, 0]
    ]

    try:
        polygon1 = Polygon(polygon1_vertices)
        print("Area of polygon1:", polygon1.calculate_area())
    except ValueError as e:
        print(e)

    try:
        polygon2 = Polygon(polygon2_vertices)
        print("Area of polygon2:", polygon2.calculate_area())
    except ValueError as e:
        print(e)