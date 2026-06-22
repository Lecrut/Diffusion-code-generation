class TriangleCalculator:
    def __init__(self, vertices):
        self.vertices = vertices

    def calculate_area(self):
        x1, y1 = self.vertices['A']
        x2, y2 = self.vertices['B']
        x3, y3 = self.vertices['C']
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

if __name__ == '__main__':
    vertices = {
        'A': (0, 0),
        'B': (4, 0),
        'C': (2, 3)
    }
    triangle = TriangleCalculator(vertices)
    area = triangle.calculate_area()
    print(area)