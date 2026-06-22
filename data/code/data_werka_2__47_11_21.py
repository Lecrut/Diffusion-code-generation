import math

class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if not all(side > 0 for side in (side_a, side_b, side_c)):
            raise ValueError('Side lengths must be positive')
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError('The given side lengths do not form a valid triangle')

    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        area = triangle.area()
        print(f'The area of the triangle with sides 3, 4, and 5 is: {area}')
    except ValueError as e:
        print(e)