class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.vertices = [(x1, y1), (x2, y2), (x3, y3)]

    def get_vertices(self):
        return self.vertices

if __name__ == '__main__':
    triangle = Triangle(0, 0, 3, 0, 1.5, 4)
    print(triangle.get_vertices())