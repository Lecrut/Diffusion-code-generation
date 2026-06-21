import math

class CircleAreaCalculator:
    PI = math.pi

    @staticmethod
    def calculate_area(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return CircleAreaCalculator.PI * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 3.5
    area = CircleAreaCalculator.calculate_area(sample_radius)
    print(area)