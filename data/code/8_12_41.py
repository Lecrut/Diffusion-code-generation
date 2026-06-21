import math

class ShapeCalculator:
    def __init__(self, shape, dimensions, scale_factor):
        self.shape = shape
        self.dimensions = dimensions
        self.scale_factor = scale_factor

    def calculate_area(self):
        if self.shape == 'rectangle':
            width, height = self.dimensions
            return width * height
        elif self.shape == 'circle':
            radius = self.dimensions[0]
            return math.pi * (radius ** 2)
        else:
            raise ValueError("Unsupported shape")

    def scaled_area(self):
        area = self.calculate_area()
        return area * self.scale_factor

if __name__ == '__main__':
    rectangle_dimensions = (5, 10)
    circle_dimensions = (7,)
    scale_factor = 2.5

    rectangle_calculator = ShapeCalculator('rectangle', rectangle_dimensions, scale_factor)
    circle_calculator = ShapeCalculator('circle', circle_dimensions, scale_factor)

    print(rectangle_calculator.scaled_area())
    print(circle_calculator.scaled_area())