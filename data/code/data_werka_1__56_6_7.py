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
        [1, 1],
        [4, 5],
        [7, 3],
        [5, -2]
    ]

    try:
        polygon1 = Polygon(polygon1_vertices)
        print(f"Area of polygon1: {polygon1.calculate_area()}")
    except ValueError as e:
        print(e)

    polygon2_vertices = [
        [0, 0],
        [6, 0],
        [3, 4]
    ]

    try:
        polygon2 = Polygon(polygon2_vertices)
        print(f"Area of polygon2: {polygon2.calculate_area()}")
    except ValueError as e:
        print(e)