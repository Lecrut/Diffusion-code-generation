import math

class CircleCalculator:
    RADIUS = 5
    
    @staticmethod
    def calculate_area(radius):
        return math.pi * radius ** 2

if __name__ == '__main__':
    area = CircleCalculator.calculate_area(CircleCalculator.RADIUS)
    print(area)