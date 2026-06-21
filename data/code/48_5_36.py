import math

class Triangle:
    EPSILON = 1e-9

    @staticmethod
    def is_close(a, b):
        return abs(a - b) < Triangle.EPSILON

    @staticmethod
    def validate_sides(leg1, leg2, hypotenuse):
        if hypotenuse <= leg1 or hypotenuse <= leg2:
            raise ValueError('Hypotenuse must be the longest side.')
        if not Triangle.is_close(leg1**2 + leg2**2, hypotenuse**2):
            raise ValueError('The given sides do not form a right-angled triangle.')

    @staticmethod
    def calculate_triangle_sides(leg1, leg2, hypotenuse):
        Triangle.validate_sides(leg1, leg2, hypotenuse)
        return (leg1, leg2, hypotenuse)

if __name__ == '__main__':
    try:
        sides = Triangle.calculate_triangle_sides(6, 8, 10)
        print(sides)
    except ValueError as e:
        print(e)