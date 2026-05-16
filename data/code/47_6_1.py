class TriangleArea:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def calculate_area(self):
        return 0.5 * self.base * self.height
if __name__ == '__main__':
    t = TriangleArea(10, 5)
    area = t.calculate_area()
    print(area)