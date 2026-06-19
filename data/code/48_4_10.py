import math

class Triangle:
    def __init__(self, sides):
        if len(sides) != 3:
            raise ValueError('Exactly three sides are required for a triangle.')
        self.sides = sorted(sides)
        self.a, self.b, self.c = self.sides
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueError('Side lengths must be positive numbers.')
        if self.a + self.b <= self.c:
            raise ValueError('The given sides do not form a valid triangle.')

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

if __name__ == '__main__':
    try:
        triangle = Triangle([3, 4, 5])
        print(f"Area of the triangle: {triangle.calculate_area()}")
    except ValueError as e:
        print(e)