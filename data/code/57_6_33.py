import math

class ShapeAreaCalculator:
    RECTANGLE = 'rectangle'
    CIRCLE = 'circle'

    @staticmethod
    def validate_dimensions(shape, dimensions):
        if shape == ShapeAreaCalculator.RECTANGLE and len(dimensions) != 2:
            raise ValueError('Rectangle requires exactly two dimensions')
        elif shape == ShapeAreaCalculator.CIRCLE and len(dimensions) != 1:
            raise ValueError('Circle requires exactly one dimension (radius)')
        else:
            return True

    def __init__(self, shape, dimensions):
        if not ShapeAreaCalculator.validate_dimensions(shape, dimensions):
            raise ValueError(f'Invalid dimensions for {shape}')
        self.shape = shape
        self.dimensions = dimensions

    def calculate_area(self):
        if self.shape == ShapeAreaCalculator.RECTANGLE:
            return self._calculate_rectangle_area()
        elif self.shape == ShapeAreaCalculator.CIRCLE:
            return self._calculate_circle_area()
        else:
            raise ValueError(f'Unsupported shape: {self.shape}')

    def _calculate_rectangle_area(self):
        length, width = self.dimensions
        return length * width

    def _calculate_circle_area(self):
        radius = self.dimensions[0]
        return math.pi * radius ** 2

if __name__ == '__main__':
    rectangle_dimensions = [5, 3]
    circle_dimensions = [4]
    
    rectangle_calculator = ShapeAreaCalculator(ShapeAreaCalculator.RECTANGLE, rectangle_dimensions)
    circle_calculator = ShapeAreaCalculator(ShapeAreaCalculator.CIRCLE, circle_dimensions)

    print("Rectangle Area:", rectangle_calculator.calculate_area())
    print("Circle Area:", circle_calculator.calculate_area())