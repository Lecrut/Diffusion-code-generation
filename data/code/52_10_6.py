import math

SHAPE_TYPE_RECTANGLE = 'rectangle'
SHAPE_TYPE_CIRCLE = 'circle'

class Shape:
    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions
        self._validate_dimensions()

    def _validate_dimensions(self):
        if self.shape_type == SHAPE_TYPE_RECTANGLE:
            if 'length' not in self.dimensions or 'width' not in self.dimensions:
                raise ValueError("Rectangle requires 'length' and 'width'")
        elif self.shape_type == SHAPE_TYPE_CIRCLE:
            if 'radius' not in self.dimensions:
                raise ValueError("Circle requires 'radius'")
        else:
            raise ValueError("Unsupported shape type")

    def _calculate_rectangle_area(self):
        length = self.dimensions['length']
        width = self.dimensions['width']
        return length * width

    def _calculate_circle_area(self):
        radius = self.dimensions['radius']
        return math.pi * (radius ** 2)

    def area(self):
        if self.shape_type == SHAPE_TYPE_RECTANGLE:
            return self._calculate_rectangle_area()
        elif self.shape_type == SHAPE_TYPE_CIRCLE:
            return self._calculate_circle_area()
        else:
            raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle = Shape(SHAPE_TYPE_RECTANGLE, length=10, width=4)
    circle = Shape(SHAPE_TYPE_CIRCLE, radius=6)

    print(f"Rectangle area: {rectangle.area()}")
    print(f"Circle area: {circle.area()}")