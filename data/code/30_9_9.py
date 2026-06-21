import math

class CircleCalculator:
    PI_VALUE = math.pi

    @staticmethod
    def compute_area(radius):
        return CircleCalculator.PI_VALUE * radius * radius

if __name__ == '__main__':
    sample_radius = 12
    area_result = CircleCalculator.compute_area(sample_radius)
    print(area_result)