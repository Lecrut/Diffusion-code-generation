import math

class GeometryCalculator:
    def __init__(self, rectangle_length, rectangle_width, circle_diameter):
        self.rectangle_length = rectangle_length
        self.rectangle_width = rectangle_width
        self.circle_diameter = circle_diameter

    def calculate_rectangle_diagonal(self):
        return math.sqrt(self.rectangle_length**2 + self.rectangle_width**2)

    def calculate_circle_radius(self):
        return self.circle_diameter / 2

    def calculate_ratio(self):
        diagonal = self.calculate_rectangle_diagonal()
        radius = self.calculate_circle_radius()
        if radius != 0:
            return diagonal / radius
        else:
            return "Undefined ratio (division by zero)"

if __name__ == '__main__':
    geometry_calculator = GeometryCalculator(rectangle_length=6, rectangle_width=8, circle_diameter=15)
    print(geometry_calculator.calculate_rectangle_diagonal())
    print(geometry_calculator.calculate_circle_radius())
    print(geometry_calculator.calculate_ratio())