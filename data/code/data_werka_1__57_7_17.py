import math

class Shape:

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

    @staticmethod
    def _calculate_rectangle_area(length, width):
        return length * width

    @staticmethod
    def _calculate_circle_area(radius):
        return math.pi * radius ** 2
if __name__ == '__main__':
    rectangle = Shape('rectangle', (5, 3))
    circle = Shape('circle', 4)
    print('Rectangle area:', rectangle.calculate_area())
    print('Circle area:', circle.calculate_area())