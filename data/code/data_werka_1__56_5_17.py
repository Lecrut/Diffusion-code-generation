import math

class GeometryCalculator:
    def calculate_rectangle_diagonal(self, length, width):
        return math.sqrt(length**2 + width**2)
    
    def calculate_circle_radius(self, diameter):
        return diameter / 2
    
    def calculate_ratio(self, rectangle_length, rectangle_width, circle_diameter):
        diagonal = self.calculate_rectangle_diagonal(rectangle_length, rectangle_width)
        radius = self.calculate_circle_radius(circle_diameter)
        if radius != 0:
            return diagonal / radius
        else:
            return "Undefined ratio (division by zero)"

if __name__ == '__main__':
    geometry_calculator = GeometryCalculator()
    
    rectangle_length = 6
    rectangle_width = 8
    circle_diameter = 15
    
    ratio = geometry_calculator.calculate_ratio(rectangle_length, rectangle_width, circle_diameter)
    print("Ratio of diagonal to radius:", ratio)