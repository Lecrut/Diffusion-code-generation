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
            x_i, y_i = self.vertices[i]
            x_j, y_j = self.vertices[j]
            area += x_i * y_j - y_i * x_j
        return abs(area) / 2.0

if __name__ == '__main__':
    polygon1_vertices = [
        [1, 6],
        [3, 1],
        [7, 2],
        [5, 4]
    ]

    polygon2_vertices = [
        [2, 3],
        [8, 5],
        [6, 9]
    ]

    polygon1 = Polygon(polygon1_vertices)
    polygon2 = Polygon(polygon2_vertices)

    print("Area of Polygon 1:", polygon1.calculate_area())
    print("Area of Polygon 2:", polygon2.calculate_area())