import math

class ShapeCalculator:
    def __init__(self, shape, dimensions):
        self.shape = shape
        self.dimensions = dimensions

    def calculate_area(self):
        if self.shape == 'rectangle':
            return self._calculate_rectangle_area()
        elif self.shape == 'circle':
            return self._calculate_circle_area()
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

if __name__ == '__main__':
    rectangle_dimensions = [5, 3]
    circle_dimensions = [4]

    rectangle_calculator = ShapeCalculator('rectangle', rectangle_dimensions)
    rectangle_area = rectangle_calculator.calculate_area()
    print(f"Rectangle area: {rectangle_area}")

    circle_calculator = ShapeCalculator('circle', circle_dimensions)
    circle_area = circle_calculator.calculate_area()
    print(f"Circle area: {circle_area}")