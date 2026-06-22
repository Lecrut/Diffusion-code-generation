import math

class Shape:
    SHAPE_RECTANGLE = 'rectangle'
    SHAPE_CIRCLE = 'circle'

    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions

    @staticmethod
    def validate_dimensions(dimensions, required_keys):
        for key in required_keys:
            if key not in dimensions or dimensions[key] is None:
                raise ValueError(f"{key} is required")

    def area(self):
        if self.shape_type == Shape.SHAPE_RECTANGLE:
            Shape.validate_dimensions(self.dimensions, ['length', 'width'])
            return self._calculate_rectangle_area()
        elif self.shape_type == Shape.SHAPE_CIRCLE:
            Shape.validate_dimensions(self.dimensions, ['radius'])
            return self._calculate_circle_area()
        else:
            raise ValueError(f"Unsupported shape type: {self.shape_type}")

    def _calculate_rectangle_area(self):
        return self.dimensions['length'] * self.dimensions['width']

    def _calculate_circle_area(self):
        return math.pi * self.dimensions['radius'] ** 2

if __name__ == '__main__':
    rectangle = Shape('rectangle', length=5, width=3)
    circle = Shape('circle', radius=4)

    print("Rectangle Area:", rectangle.area())
    print("Circle Area:", circle.area())