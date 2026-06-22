import math

class CircleCalculator:
    def __init__(self):
        self.results = {}

    def calculate_area(self, radius):
        if not isinstance(radius, (int, float)):
            raise ValueError("Radius must be a number.")
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        area = math.pi * (radius ** 2)
        self.results[radius] = area
        return area

if __name__ == '__main__':
    calculator = CircleCalculator()
    radii = [3.0, 5.5, 7.8, -1.0, 'a']
    for radius in radii:
        try:
            area = calculator.calculate_area(radius)
            print(f"Radius: {radius}, Area: {area}")
        except ValueError as e:
            print(f"Error with radius {radius}: {e}")