import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

class CircleCalculator:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return calculate_circle_area(self.radius)

if __name__ == '__main__':
    try:
        sample_radius = 5.0
        calculator = CircleCalculator(sample_radius)
        print(f"The area of a circle with radius {sample_radius} is {calculator.area()}")
        
        invalid_radius = -3.0
        calculator_invalid = CircleCalculator(invalid_radius)
        print(calculator_invalid.area())
    except ValueError as e:
        print(e)