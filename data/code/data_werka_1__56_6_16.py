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
            area += x_i * y_j - x_j * y_i
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
        [5, 5],
        [1, 5]
    ]

    polygon1 = Polygon(polygon1_vertices)
    polygon2 = Polygon(polygon2_vertices)

    print("Area of Polygon 1:", polygon1.calculate_area())
    print("Area of Polygon 2:", polygon2.calculate_area())