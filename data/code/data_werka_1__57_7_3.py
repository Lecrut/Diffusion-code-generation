import math

class ShapeCalculator:

    def __init__(self, shape_type, dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions

    def calculate_area(self):
        if self.shape_type == 'rectangle':
            return self._calculate_rectangle_area()
        elif self.shape_type == 'circle':
            return self._calculate_circle_area()
        else:
            raise ValueError('Unsupported shape type')

    def _calculate_rectangle_area(self):
        length, width = self.dimensions
        return length * width

    def _calculate_circle_area(self):
        radius = self.dimensions[0]
        return math.pi * radius ** 2
if __name__ == '__main__':
    rectangle_dimensions = (5, 3)
    circle_dimensions = (4,)
    rectangle_calculator = ShapeCalculator('rectangle', rectangle_dimensions)
    circle_calculator = ShapeCalculator('circle', circle_dimensions)
    print('Rectangle Area:', rectangle_calculator.calculate_area())
    print('Circle Area:', circle_calculator.calculate_area())