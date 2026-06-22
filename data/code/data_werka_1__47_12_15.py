import math

class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if not self.is_valid_triangle():
            raise ValueError('The given sides do not form a valid triangle')

    def is_valid_triangle(self):
        return (self.side_a > 0 and self.side_b > 0 and self.side_c > 0 and
                self.side_a + self.side_b > self.side_c and
                self.side_a + self.side_c > self.side_b and
                self.side_b + self.side_c > self.side_a)

    def calculate_area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        area = math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
        return area

if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        area = triangle.calculate_area()
        print(area)
    except ValueError as e:
        print(e)