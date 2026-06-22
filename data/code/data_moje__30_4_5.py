import math

class CircleAreaCalculator:
    PI = math.pi

    @staticmethod
    def compute_area(radius):
        squared = radius * radius
        return CircleAreaCalculator.PI * squared

if __name__ == '__main__':
    test_radius = 12.5
    area_result = CircleAreaCalculator.compute_area(test_radius)
    print(area_result)