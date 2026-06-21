import math

class ShapeCalculator:
    def __init__(self, shape, dimensions):
        self.shape = shape.lower()
        self.dimensions = dimensions

    def calculate_area(self):
        if self.shape == 'rectangle':
            return self._calculate_rectangle_area()
        elif self.shape == 'circle':
            return self._calculate_circle_area()
        elif self.shape == 'triangle':
            return self._calculate_triangle_area()
        else:
            raise ValueError(f'Unsupported shape: {self.shape}')

    def _calculate_rectangle_area(self):
        if len(self.dimensions) != 2:
            raise ValueError('Rectangle requires exactly two dimensions')
        length, width = self.dimensions
        return length * width

    def _calculate_circle_area(self):
        if len(self.dimensions) != 1:
            raise ValueError('Circle requires exactly one dimension (radius)')
        radius = self.dimensions[0]
        return math.pi * radius ** 2

    def _calculate_triangle_area(self):
        if len(self.dimensions) != 2:
            raise ValueError('Triangle requires exactly two dimensions (base and height)')
        base, height = self.dimensions
        return 0.5 * base * height

if __name__ == '__main__':
    rectangle_dimensions = [5, 3]
    circle_dimensions = [4]
    triangle_dimensions = [8, 4]

    rectangle_calculator = ShapeCalculator('rectangle', rectangle_dimensions)
    circle_calculator = ShapeCalculator('circle', circle_dimensions)
    triangle_calculator = ShapeCalculator('triangle', triangle_dimensions)

    print("Rectangle Area:", rectangle_calculator.calculate_area())
    print("Circle Area:", circle_calculator.calculate_area())
    print("Triangle Area:", triangle_calculator.calculate_area())