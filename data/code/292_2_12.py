class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @staticmethod
    def semi_perimeter(a, b, c):
        return (a + b + c) / 2

    @staticmethod
    def area_squared(a, b, c):
        s = Triangle.semi_perimeter(a, b, c)
        return s * (s - a) * (s - b) * (s - c)

    def perimeter(self):
        return self.area_squared(self.side1, self.side2, self.side3) ** 0.5

if __name__ == '__main__':
    triangle = Triangle(3, 4, 5)
    print(triangle.perimeter())