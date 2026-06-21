import math

class TriangleAreaCalculator:
    MIN_SIDES = 3
    MAX_SIDES = 3

    @staticmethod
    def is_valid_triangle(sides):
        a, b, c = sides
        return a + b > c and a + c > b and b + c > a

    @staticmethod
    def calculate_area_with_heron(sides):
        if len(sides) != TriangleAreaCalculator.MIN_SIDES:
            raise ValueError('Exactly three sides are required to form a triangle.')
        if any(side <= 0 for side in sides):
            raise ValueError('Side lengths must be positive numbers.')
        if not TriangleAreaCalculator.is_valid_triangle(sides):
            raise ValueError('The given sides do not form a valid triangle.')
        s = sum(sides) / 2
        area = math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))
        return area

if __name__ == '__main__':
    try:
        sides = [6, 8, 10]
        calculator = TriangleAreaCalculator()
        area = calculator.calculate_area_with_heron(sides)
        print(area)
    except ValueError as e:
        print(e)