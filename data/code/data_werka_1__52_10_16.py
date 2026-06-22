import math

class Shape:
    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions
        if not self._validate_dimensions():
            raise ValueError("Invalid dimensions for the given shape type")

    def _validate_dimensions(self):
        if self.shape_type == 'rectangle':
            return 'length' in self.dimensions and 'width' in self.dimensions
        elif self.shape_type == 'circle':
            return 'radius' in self.dimensions
        else:
            raise ValueError("Unsupported shape type")

    def area(self):
        if self.shape_type == 'rectangle':
            return self._calculate_rectangle_area()
        elif self.shape_type == 'circle':
            return self._calculate_circle_area()

    def _calculate_rectangle_area(self):
        return self.dimensions['length'] * self.dimensions['width']

    def _calculate_circle_area(self):
        return math.pi * (self.dimensions['radius'] ** 2)

if __name__ == '__main__':
    rectangle = Shape('rectangle', length=4, width=6)
    circle = Shape('circle', radius=5)
    print("Rectangle area:", rectangle.area())
    print("Circle area:", circle.area())