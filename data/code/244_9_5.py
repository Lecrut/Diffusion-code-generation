class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    def area(self):
        n = len(self.vertices)
        area = 0.5 * abs(sum(x * y2 - y * x2 for (x, y), (x2, y2) in zip(self.vertices, self.vertices[1:] + self.vertices[:1])))
        return area

if __name__ == '__main__':
    polygon1 = Polygon([(0, 0), (4, 0), (4, 3), (0, 3)])
    polygon2 = Polygon([(1, 1), (5, 1), (5, 4), (1, 4)])

    total_area = polygon1.area() + polygon2.area()
    print(total_area)