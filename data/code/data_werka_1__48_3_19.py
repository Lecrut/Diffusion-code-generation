import math

class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = (x1, y1)
        self.x2, self.y2 = (x2, y2)
        self.x3, self.y3 = (x3, y3)
        self.a = self.distance(x1, y1, x2, y2)
        self.b = self.distance(x2, y2, x3, y3)
        self.c = self.distance(x3, y3, x1, y1)

    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def is_valid(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueError('Side lengths must be positive.')
        if not (self.a + self.b > self.c and self.a + self.c > self.b and (self.b + self.c > self.a)):
            raise ValueError('The given points do not form a valid triangle.')

    def side_lengths(self):
        return (self.a, self.b, self.c)
if __name__ == '__main__':
    try:
        triangle = Triangle(0, 0, 3, 4, 6, 0)
        triangle.is_valid()
        sides = triangle.side_lengths()
        print(f'Side lengths: {sides}')
    except ValueError as e:
        print(e)