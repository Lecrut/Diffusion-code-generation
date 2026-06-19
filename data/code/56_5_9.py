import math

class GeometryCalculator:
    def calculate_rectangle_diagonal(self, length, width):
        return math.sqrt(length**2 + width**2)
    
    def calculate_circle_radius(self, diameter):
        return diameter / 2

if __name__ == '__main__':
    calculator = GeometryCalculator()
    rectangle_length = 6
    rectangle_width = 8
    circle_diameter = 15
    
    diagonal = calculator.calculate_rectangle_diagonal(rectangle_length, rectangle_width)
    radius = calculator.calculate_circle_radius(circle_diameter)
    
    if radius != 0:
        ratio = diagonal / radius
        print(ratio)
    else:
        print("Undefined ratio (division by zero)")