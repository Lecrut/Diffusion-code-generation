class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    def calculate_area(self):
        n = len(self.vertices)
        if n < 3:
            return 0.0
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += self.vertices[i][0] * self.vertices[j][1]
            area -= self.vertices[j][0] * self.vertices[i][1]
        return abs(area) / 2.0

if __name__ == '__main__':
    polygon1_vertices = [
        [0, 0],
        [4, 0],
        [4, 3],
        [0, 3]
    ]
    polygon2_vertices = [
        [1, 1],
        [5, 1],
        [5, 4],
        [1, 4]
    ]

    polygon1 = Polygon(polygon1_vertices)
    polygon2 = Polygon(polygon2_vertices)

    print("Area of polygon1:", polygon1.calculate_area())
    print("Area of polygon2:", polygon2.calculate_area())