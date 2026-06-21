import math

class Triangle:
    def __init__(self, sides):
        if len(sides) != 3:
            raise ValueError('Exactly three sides are required to form a triangle.')
        if any(side <= 0 for side in sides):
            raise ValueError('Side lengths must be positive numbers.')
        if not self.is_valid_triangle(sides):
            raise ValueError('The given sides do not form a valid triangle.')
        self.sides = sides

    def is_valid_triangle(self, sides):
        a, b, c = sides
        return a + b > c and a + c > b and b + c > a

    def calculate_area(self):
        s = sum(self.sides) / 2
        area = math.sqrt(s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2]))
        return area

if __name__ == '__main__':
    try:
        triangle1 = Triangle([3, 4, 5])
        print(triangle1.calculate_area())

        triangle2 = Triangle([7, 10, 5])
        print(triangle2.calculate_area())
    except ValueError as e:
        print(e)