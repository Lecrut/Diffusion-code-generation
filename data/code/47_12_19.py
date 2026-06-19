import math

class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self._validate_sides()

    def _validate_sides(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueError('Side lengths must be positive')
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            raise ValueError('The given sides do not form a valid triangle')

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area
if __name__ == '__main__':
    try:
        t = Triangle(3, 4, 5)
        area = t.calculate_area()
        print(f'The area of the triangle with sides 3, 4, and 5 is: {area}')
        t2 = Triangle(6, 8, 10)
        area2 = t2.calculate_area()
        print(f'The area of the triangle with sides 6, 8, and 10 is: {area2}')
    except ValueError as e:
        print(e)