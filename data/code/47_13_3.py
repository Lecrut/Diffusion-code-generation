class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        x1, y1 = self.p1
        x2, y2 = self.p2
        x3, y3 = self.p3
        return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)

if __name__ == '__main__':
    try:
        vertices = [(0, 0), (4, 0), (2, 3)]
        triangle = Triangle(*vertices)
        area = triangle.area()
        print(f"Area of the triangle: {area:.2f}")
    except Exception as e:
        print(f"Error: {e}")