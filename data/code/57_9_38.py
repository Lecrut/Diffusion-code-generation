import math

class CircleCalculator:
    @staticmethod
    def calculate_area(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 3.5
    area = CircleCalculator.calculate_area(sample_radius)
    print(area)