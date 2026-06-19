class Triangle:
    def __init__(self, vertices):
        self.vertices = vertices

    def area(self):
        x1, y1 = self.vertices[0]
        x2, y2 = self.vertices[1]
        x3, y3 = self.vertices[2]
        return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)

if __name__ == '__main__':
    vertices = [(0, 0), (4, 0), (2, 3)]
    triangle = Triangle(vertices)
    area = triangle.area()
    print(f"Area of the triangle: {area:.2f}")