import math

def calculate_rectangle_diagonal(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers")
    return math.sqrt(length**2 + width**2)

def calculate_circle_radius(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be a positive number")
    return diameter / 2

class GeometryCalculator:
    def __init__(self, rectangle_length, rectangle_width, circle_diameter):
        self.diagonal = calculate_rectangle_diagonal(rectangle_length, rectangle_width)
        self.radius = calculate_circle_radius(circle_diameter)

    def calculate_ratio(self):
        if self.radius == 0:
            raise ValueError("Undefined ratio (division by zero)")
        return self.diagonal / self.radius

if __name__ == '__main__':
    try:
        calculator = GeometryCalculator(rectangle_length=6, rectangle_width=8, circle_diameter=15)
        ratio = calculator.calculate_ratio()
        print(ratio)
    except ValueError as e:
        print(e)