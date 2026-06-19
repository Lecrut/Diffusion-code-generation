import math

class Shape:
    SHAPE_TYPES = {
        'rectangle': 'calculate_rectangle_area',
        'circle': 'calculate_circle_area'
    }

    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions
        self._validate_dimensions()

    def _validate_dimensions(self):
        if self.shape_type not in self.SHAPE_TYPES:
            raise ValueError("Unsupported shape type")
        required_keys = getattr(self, f'_{self.shape_type}_required_keys')
        for key in required_keys:
            if key not in self.dimensions:
                raise ValueError(f"{self.shape_type.capitalize()} requires '{key}'")

    @staticmethod
    def calculate_rectangle_area(length, width):
        return length * width

    @staticmethod
    def calculate_circle_area(radius):
        return math.pi * (radius ** 2)

    def area(self):
        method_name = self.SHAPE_TYPES[self.shape_type]
        method = getattr(self, method_name)
        return method(**self.dimensions)

if __name__ == '__main__':
    rectangle = Shape('rectangle', length=6, width=4)
    circle = Shape('circle', radius=5)

    print("Rectangle Area:", rectangle.area())
    print("Circle Area:", circle.area())