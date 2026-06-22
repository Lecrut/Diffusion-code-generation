import math

class CircleCalculator:
    PI = math.pi

    @staticmethod
    def calculate_area(radius):
        return CircleCalculator.PI * radius ** 2

if __name__ == '__main__':
    print(CircleCalculator.calculate_area(7))