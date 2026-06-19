import math
PI = 3.141592653589793

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

    def _calculate_rectangle_area(self):
        length, width = self.dimensions
        return length * width

    def _calculate_circle_area(self):
        radius = self.dimensions[0]
        return PI * radius ** 2
if __name__ == '__main__':
    rectangle = Shape('rectangle', (5, 3))
    circle = Shape('circle', (4,))
    print(f'Rectangle area: {rectangle.calculate_area()}')
    print(f'Circle area: {circle.calculate_area()}')