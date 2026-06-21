import math

class AreaCalculator:
    def __init__(self, shape, dimensions):
        self.shape = shape
        self.dimensions = dimensions
        self._validate_dimensions()

    def _validate_dimensions(self):
        if self.shape == 'rectangle':
            if len(self.dimensions) != 2:
                raise ValueError('Rectangle requires exactly two dimensions')
        elif self.shape == 'circle':
            if len(self.dimensions) != 1:
                raise ValueError('Circle requires exactly one dimension (radius)')
        else:
            raise ValueError(f'Unsupported shape: {self.shape}')

    def calculate_area(self):
        if self.shape == 'rectangle':
            return self._calculate_rectangle_area()
        elif self.shape == 'circle':
            return self._calculate_circle_area()

    def _calculate_rectangle_area(self):
        length, width = self.dimensions
        return length * width

    def _calculate_circle_area(self):
        radius = self.dimensions[0]
        return math.pi * radius ** 2

if __name__ == '__main__':
    rectangle_dimensions = [5, 3]
    circle_dimensions = [4]

    rectangle_calculator = AreaCalculator('rectangle', rectangle_dimensions)
    circle_calculator = AreaCalculator('circle', circle_dimensions)

    print("Rectangle Area:", rectangle_calculator.calculate_area())
    print("Circle Area:", circle_calculator.calculate_area())