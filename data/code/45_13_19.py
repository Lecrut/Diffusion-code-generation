import math

class CircleAreaCalculator:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    def compute_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    try:
        radius_value = 5.0
        calculator = CircleAreaCalculator(radius_value)
        area_result = calculator.compute_area()
        print(area_result)
    except ValueError as e:
        print(e)