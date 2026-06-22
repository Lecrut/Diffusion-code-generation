class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    def area(self):
        n = len(self.vertices)
        if n < 3:
            return 0
        area = 0
        for i in range(n):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % n]
            area += x1 * y2 - y1 * x2
        return abs(area) / 2

if __name__ == '__main__':
    polygon1 = Polygon([(0, 0), (4, 0), (4, 3), (0, 3)])
    polygon2 = Polygon([(1, 1), (5, 1), (5, 4), (1, 4)])

    print("Area of polygon1:", polygon1.area())
    print("Area of polygon2:", polygon2.area())