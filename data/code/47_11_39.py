import math

class Triangle:

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if not all((side > 0 for side in (side_a, side_b, side_c))):
            raise ValueError('Side lengths must be positive')
        if self._is_valid_triangle():
            raise ValueError('The given side lengths do not form a valid triangle')

    def _is_valid_triangle(self):
        return self.side_a + self.side_b <= self.side_c or self.side_a + self.side_c <= self.side_b or self.side_b + self.side_c <= self.side_a

    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
if __name__ == '__main__':
    try:
        triangle1 = Triangle(3, 4, 5)
        print(f'The area of the triangle with sides 3, 4, and 5 is: {triangle1.area()}')
        triangle2 = Triangle(1, 1, 3)
    except ValueError as e:
        print(e)