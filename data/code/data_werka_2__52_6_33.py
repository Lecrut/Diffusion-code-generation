import math

class Shape:
    SHAPE_RECTANGLE = 'rectangle'
    SHAPE_CIRCLE = 'circle'

    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions

    def area(self):
        if self.shape_type == self.SHAPE_RECTANGLE:
            length = self.dimensions.get('length')
            width = self.dimensions.get('width')
            if length is None or width is None:
                raise ValueError('Rectangle requires both length and width.')
            return self._calculate_rectangle_area(length, width)
        elif self.shape_type == self.SHAPE_CIRCLE:
            radius = self.dimensions.get('radius')
            if radius is None:
                raise ValueError('Circle requires a radius.')
            return self._calculate_circle_area(radius)
        else:
            raise ValueError(f"Unsupported shape type: {self.shape_type}")

    @staticmethod
    def _calculate_rectangle_area(length, width):
        return length * width

    @staticmethod
    def _calculate_circle_area(radius):
        return math.pi * radius ** 2

if __name__ == '__main__':
    rectangle = Shape('rectangle', length=5, width=3)
    circle = Shape('circle', radius=4)

    print(f"Rectangle area: {rectangle.area()}")
    print(f"Circle area: {circle.area()}")