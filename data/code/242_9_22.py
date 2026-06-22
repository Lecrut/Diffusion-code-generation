import math

class GeometryCalculator:
    def __init__(self, semicircle_radius, rectangle_width, rectangle_height):
        self.semicircle_radius = semicircle_radius
        self.rectangle_width = rectangle_width
        self.rectangle_height = rectangle_height
    
    def semicircle_area(self):
        return 0.5 * math.pi * self.semicircle_radius ** 2
    
    def rectangle_area(self):
        return self.rectangle_width * self.rectangle_height

if __name__ == '__main__':
    calculator = GeometryCalculator(4, 6, 3)
    print(f"Semicircle area: {calculator.semicircle_area():.10f}")
    print(f"Rectangle area: {calculator.rectangle_area():.10f}")