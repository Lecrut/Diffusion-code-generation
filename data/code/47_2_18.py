import math

class Triangle:
    def __init__(self, a, b, c):
        if not self.is_valid_triangle(a, b, c):
            raise ValueError('The given side lengths do not form a valid triangle.')
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

if __name__ == '__main__':
    try:
        triangle = Triangle(6, 8, 10)
        area = triangle.calculate_area()
        print(area)
    except ValueError as e:
        print(e)