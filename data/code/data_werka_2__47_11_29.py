import math

class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self._validate_sides()

    def _validate_sides(self):
        if not all(side > 0 for side in (self.side_a, self.side_b, self.side_c)):
            raise ValueError('Side lengths must be positive')
        if self.side_a + self.side_b <= self.side_c or self.side_a + self.side_c <= self.side_b or self.side_b + self.side_c <= self.side_a:
            raise ValueError('The given side lengths do not form a valid triangle')

    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

if __name__ == '__main__':
    try:
        triangle = Triangle(7, 10, 5)
        area = triangle.area()
        perimeter = triangle.perimeter()
        print(f'The area of the triangle with sides 7, 10, and 5 is: {area}')
        print(f'The perimeter of the triangle with sides 7, 10, and 5 is: {perimeter}')
    except ValueError as e:
        print(e)