import math

class Shape:
    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions
        self._validate_dimensions()

    def _validate_dimensions(self):
        if self.shape_type == 'rectangle':
            if 'length' not in self.dimensions or 'width' not in self.dimensions:
                raise ValueError('Rectangle requires both length and width')
        elif self.shape_type == 'circle':
            if 'radius' not in self.dimensions:
                raise ValueError('Circle requires a radius')
        else:
            raise ValueError(f"Unsupported shape type: {self.shape_type}")

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
    rectangle = Shape('rectangle', length=5, width=3)
    circle = Shape('circle', radius=4)

    print("Rectangle Area:", rectangle.area())
    print("Circle Area:", circle.area())