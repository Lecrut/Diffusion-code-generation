import math

class Triangle:
    def __init__(self, sides):
        if len(sides) != 3:
            raise ValueError('Exactly three sides are required for a triangle.')
        self.a, self.b, self.c = sorted(sides)
        if not (self.a + self.b > self.c):
            raise ValueError('The given sides do not form a valid triangle.')

    @staticmethod
    def is_valid_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

if __name__ == '__main__':
    try:
        sides = [3, 4, 5]
        triangle = Triangle(sides)
        print(triangle.calculate_area())
    except ValueError as e:
        print(e)