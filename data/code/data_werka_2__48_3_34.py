import math

class Triangle:
    MIN_VALID_SIDE_LENGTH = 0.01

    @staticmethod
    def is_valid_triangle(sides):
        a, b, c = sides
        return a + b > c and a + c > b and b + c > a

    @staticmethod
    def calculate_area_with_heron(sides):
        if len(sides) != 3:
            raise ValueError('Exactly three sides are required to form a triangle.')
        for side in sides:
            if side <= Triangle.MIN_VALID_SIDE_LENGTH:
                raise ValueError('Side lengths must be positive numbers greater than 0.01.')
        if not Triangle.is_valid_triangle(sides):
            raise ValueError('The given sides do not form a valid triangle.')
        s = sum(sides) / 2
        area = math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))
        return area

if __name__ == '__main__':
    try:
        sides = [3, 4, 5]
        triangle = Triangle()
        area = triangle.calculate_area_with_heron(sides)
        print(area)
    except ValueError as e:
        print(e)