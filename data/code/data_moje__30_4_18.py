import math

class CircleAreaCalculator:
    PI = math.pi

    @staticmethod
    def compute_area(radius):
        radius_squared = radius * radius
        return CircleAreaCalculator.PI * radius_squared

if __name__ == '__main__':
    test_radius = 10
    area_value = CircleAreaCalculator.compute_area(test_radius)
    print(area_value)