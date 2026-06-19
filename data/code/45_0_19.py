import math

class CircleCalculator:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

def calculate_circle_area(radius):
    calculator = CircleCalculator(radius)
    return calculator.area()

if __name__ == '__main__':
    sample_radius1 = 4.5
    sample_radius2 = 6.0
    try:
        area1 = calculate_circle_area(sample_radius1)
        area2 = calculate_circle_area(sample_radius2)
        print(f"Area for radius {sample_radius1}: {area1}")
        print(f"Area for radius {sample_radius2}: {area2}")
    except ValueError as e:
        print(e)