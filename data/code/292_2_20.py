class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @staticmethod
    def semi_perimeter(a, b, c):
        return (a + b + c) / 2

    def area(self):
        s = Triangle.semi_perimeter(self.side1, self.side2, self.side3)
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

if __name__ == '__main__':
    triangle = Triangle(3, 4, 5)
    print(triangle.area())