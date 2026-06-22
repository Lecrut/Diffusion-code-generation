import math

class Shape:
    @staticmethod
    def rectangle_area(width, height):
        return width * height

    @staticmethod
    def circle_area(radius):
        return math.pi * (radius ** 2)

class ScaledAreaCalculator:
    def __init__(self, shape, dimensions, scale_factor):
        self.shape = shape
        self.dimensions = dimensions
        self.scale_factor = scale_factor

    def calculate_scaled_area(self):
        if self.shape == 'rectangle':
            area = Shape.rectangle_area(*self.dimensions)
        elif self.shape == 'circle':
            area = Shape.circle_area(*self.dimensions)
        else:
            raise ValueError("Unsupported shape")
        return area * self.scale_factor

if __name__ == '__main__':
    rectangle_dimensions = (5, 10)
    circle_dimensions = (7,)
    scale_factor = 2.5
    rectangle_calculator = ScaledAreaCalculator('rectangle', rectangle_dimensions, scale_factor)
    circle_calculator = ScaledAreaCalculator('circle', circle_dimensions, scale_factor)

    print(rectangle_calculator.calculate_scaled_area())
    print(circle_calculator.calculate_scaled_area())