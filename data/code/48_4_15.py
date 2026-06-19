import math

class Triangle:
    MIN_VALID_SIDE = 0.1

    @staticmethod
    def is_valid_triangle(sides):
        if len(sides) != 3:
            return False
        a, b, c = sides
        return all(side > Triangle.MIN_VALID_SIDE for side in sides) and (a + b > c) and (a + c > b) and (b + c > a)

    @staticmethod
    def calculate_area(sides):
        if not Triangle.is_valid_triangle(sides):
            raise ValueError('The given sides do not form a valid triangle.')
        a, b, c = sides
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

if __name__ == '__main__':
    try:
        sides = [3, 4, 5]
        area = Triangle.calculate_area(sides)
        print(area)
    except ValueError as e:
        print(e)