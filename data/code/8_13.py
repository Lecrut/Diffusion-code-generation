import math

class ShapeCalculator:
    def __init__(self, length, width, radius):
        self.length = length
        self.width = width
        self.radius = radius

    def calculate_scaled_rectangle_area(self, scale_factor):
        if scale_factor <= 0:
            raise ValueError("Scale factor must be positive")
        return (self.length * scale_factor) * (self.width * scale_factor)

    def calculate_scaled_circle_area(self, scale_factor):
        if scale_factor <= 0:
            raise ValueError("Scale factor must be positive")
        return math.pi * (self.radius * scale_factor) ** 2

if __name__ == '__main__':
    length = 10
    width = 5
    radius = 7
    scale_factor = 2.5
    calculator = ShapeCalculator(length, width, radius)
    print(calculator.calculate_scaled_rectangle_area(scale_factor))
    print(calculator.calculate_scaled_circle_area(scale_factor))