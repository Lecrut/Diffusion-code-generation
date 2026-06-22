import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if not self.is_valid_triangle():
            raise ValueError('The given sides do not form a valid triangle')

    def is_valid_triangle(self):
        return (self.side1 + self.side2 > self.side3 and
                self.side1 + self.side3 > self.side2 and
                self.side2 + self.side3 > self.side1)

    @staticmethod
    def calculate_area(side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError('Side lengths must be positive')
        s = (side1 + side2 + side3) / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area

    def get_area(self):
        return Triangle.calculate_area(self.side1, self.side2, self.side3)

if __name__ == '__main__':
    try:
        triangle = Triangle(7, 10, 5)
        print(triangle.get_area())
    except ValueError as e:
        print(e)