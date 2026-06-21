import math

def validate_positive_numbers(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")

class RightAngledTriangleCalculator:
    def __init__(self, base, height):
        validate_positive_numbers(base, height)
        self.base = base
        self.height = height

    def calculate_hypotenuse(self):
        return math.sqrt(self.base**2 + self.height**2)

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        triangle_properties = {
            'base': 6.0,
            'height': 8.0
        }
        calculator = RightAngledTriangleCalculator(triangle_properties['base'], triangle_properties['height'])
        hypotenuse = calculator.calculate_hypotenuse()
        area = calculator.calculate_area()
        print(f"Hypotenuse: {hypotenuse}")
        print(f"Area: {area}")
    except ValueError as e:
        print(e)