import math

class CircleCalculator:
    PI = math.pi

    @staticmethod
    def square(value):
        return value ** 2

    @classmethod
    def calculate_area(cls, radius):
        return cls.PI * cls.square(radius)

if __name__ == '__main__':
    sample_radius = 10
    area_result = CircleCalculator.calculate_area(sample_radius)
    print(area_result)