import math

class AreaCalculator:
    CIRCLE_RADIUS = 5
    SQUARE_SIDE_LENGTH = 4

    @staticmethod
    def calculate_area_circle(radius):
        return math.pi * radius ** 2

    @staticmethod
    def calculate_area_square(side_length):
        return side_length ** 2

    @classmethod
    def total_area(cls):
        circle_area = cls.calculate_area_circle(cls.CIRCLE_RADIUS)
        square_area = cls.calculate_area_square(cls.SQUARE_SIDE_LENGTH)
        return circle_area + square_area

if __name__ == '__main__':
    calculator = AreaCalculator()
    print(calculator.total_area())