class Triangle:
    def __init__(self):
        self.vertices = [(0, 0), (4, 0), (0, 3)]

    def compute_area(self):
        x1, y1 = self.vertices[0]
        x2, y2 = self.vertices[1]
        x3, y3 = self.vertices[2]
        return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

if __name__ == '__main__':
    triangle = Triangle()
    area = triangle.compute_area()
    print(area)