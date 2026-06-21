import math

class Shape:
    RECTANGLE = 'rectangle'
    CIRCLE = 'circle'

    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions

    def area(self):
        if self.shape_type == self.RECTANGLE:
            return self._calculate_rectangle_area()
        elif self.shape_type == self.CIRCLE:
            return self._calculate_circle_area()
        else:
            raise ValueError(f"Unsupported shape type: {self.shape_type}")

    def _calculate_rectangle_area(self):
        length = self.dimensions.get('length')
        width = self.dimensions.get('width')
        if length is None or width is None:
            raise ValueError('Rectangle requires both length and width.')
        return length * width

    def _calculate_circle_area(self):
        radius = self.dimensions.get('radius')
        if radius is None:
            raise ValueError('Circle requires a radius.')
        return math.pi * radius ** 2

if __name__ == '__main__':
    rectangle = Shape(shape_type='rectangle', length=5, width=3)
    print("Rectangle Area:", rectangle.area())

    circle = Shape(shape_type='circle', radius=4)
    print("Circle Area:", circle.area())