import math

class CircleCalculator:
    PI = math.pi

    @staticmethod
    def calculate_area(radius):
        return CircleCalculator.PI * (radius ** 2)

if __name__ == '__main__':
    radius = 4.5
    area = CircleCalculator.calculate_area(radius)
    print(area)