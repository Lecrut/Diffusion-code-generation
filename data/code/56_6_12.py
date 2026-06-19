class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    def calculate_area(self):
        n = len(self.vertices)
        if n < 3:
            return 0.0
        area = sum(
            self.vertices[i][0] * self.vertices[(i + 1) % n][1]
            - self.vertices[(i + 1) % n][0] * self.vertices[i][1]
            for i in range(n)
        )
        return abs(area) / 2.0

if __name__ == '__main__':
    polygon1_vertices = [
        [1, 5],
        [4, 7],
        [8, 3],
        [2, 2]
    ]
    
    polygon2_vertices = [
        [0, 0],
        [6, 0],
        [3, 9]
    ]

    polygon1 = Polygon(polygon1_vertices)
    polygon2 = Polygon(polygon2_vertices)

    print("Area of Polygon 1:", polygon1.calculate_area())
    print("Area of Polygon 2:", polygon2.calculate_area())