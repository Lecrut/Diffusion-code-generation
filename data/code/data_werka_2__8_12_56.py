import math

class AreaCalculator:
    def __init__(self, shape, dimensions, scale_factor):
        self.shape = shape
        self.dimensions = dimensions
        self.scale_factor = scale_factor

    def calculate_area(self):
        if self.shape == 'rectangle':
            return self._calculate_rectangle_area()
        elif self.shape == 'circle':
            return self._calculate_circle_area()
        else:
            raise ValueError("Unsupported shape")

    def _calculate_rectangle_area(self):
        width, height = self.dimensions
        return width * height

    def _calculate_circle_area(self):
        radius = self.dimensions[0]
        return math.pi * (radius ** 2)

    def scaled_area(self):
        area = self.calculate_area()
        return area * self.scale_factor

if __name__ == '__main__':
    rectangle_dimensions = (3, 7)
    circle_dimensions = (6,)
    scale_factor = 1.8
    rectangle_calculator = AreaCalculator('rectangle', rectangle_dimensions, scale_factor)
    circle_calculator = AreaCalculator('circle', circle_dimensions, scale_factor)

    print(rectangle_calculator.scaled_area())
    print(circle_calculator.scaled_area())