class TriangleCalculator:
    @staticmethod
    def semi_perimeter(a, b, c):
        return (a + b + c) / 2

    @staticmethod
    def area(a, b, c):
        s = TriangleCalculator.semi_perimeter(a, b, c)
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

if __name__ == '__main__':
    triangle = TriangleCalculator()
    print(triangle.area(3, 4, 5))