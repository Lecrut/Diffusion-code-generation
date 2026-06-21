import math

class CircleCalculator:
    def compute_area(self, radius: float) -> float:
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        return math.pi * (radius * radius)

def calculate_circle_area(radius: float) -> float:
    calculator = CircleCalculator()
    return calculator.compute_area(radius)

if __name__ == '__main__':
    test_radius_one = 7.5
    area_one = calculate_circle_area(test_radius_one)
    print(area_one)
    test_radius_two = 12.0
    area_two = calculate_circle_area(test_radius_two)
    print(area_two)