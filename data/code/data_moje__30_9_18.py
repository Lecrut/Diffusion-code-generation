import math

class CircleCalculator:
    PI_VALUE = math.pi

    @staticmethod
    def compute_area(radius):
        return CircleCalculator.PI_VALUE * (radius ** 2)

if __name__ == '__main__':
    test_radius = 12
    calculated_area = CircleCalculator.compute_area(test_radius)
    print(calculated_area)