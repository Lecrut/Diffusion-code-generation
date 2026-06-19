class TriangleUtils:

    @staticmethod
    def is_valid_triangle(a, b, c):
        return a + b > c and a + c > b and (b + c > a) and (a > 0) and (b > 0) and (c > 0)

    @staticmethod
    def calculate_perimeter(a, b, c):
        if TriangleUtils.is_valid_triangle(a, b, c):
            return a + b + c
        else:
            return None

class TriangleCalculator:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return TriangleUtils.calculate_perimeter(self.a, self.b, self.c)
if __name__ == '__main__':
    triangle1 = TriangleCalculator(3, 4, 5)
    print(triangle1.perimeter())
    triangle2 = TriangleCalculator(5, 12, 13)
    print(triangle2.perimeter())
    triangle3 = TriangleCalculator(1, 2, 10)
    print(triangle3.perimeter())