import math

class AreaCalculator:
    CIRCLE_RADIUS = 5
    SQUARE_SIDE_LENGTH = 4
    
    @staticmethod
    def calculate_circle_area(radius):
        return math.pi * radius ** 2
    
    @staticmethod
    def calculate_square_area(side_length):
        return side_length ** 2
    
    @staticmethod
    def total_area():
        circle_area = AreaCalculator.calculate_circle_area(AreaCalculator.CIRCLE_RADIUS)
        square_area = AreaCalculator.calculate_square_area(AreaCalculator.SQUARE_SIDE_LENGTH)
        return circle_area + square_area

if __name__ == '__main__':
    print(AreaCalculator.total_area())