import math

class Shape:
    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions
        self._validate_dimensions()

    def _validate_dimensions(self):
        if self.shape_type == 'rectangle':
            required_keys = {'length', 'width'}
        elif self.shape_type == 'circle':
            required_keys = {'radius'}
        else:
            raise ValueError("Unsupported shape type")
        
        if not required_keys.issubset(self.dimensions.keys()):
            missing_keys = required_keys - self.dimensions.keys()
            raise ValueError(f"Missing dimensions: {', '.join(missing_keys)}")

    def area(self):
        if self.shape_type == 'rectangle':
            return self._calculate_rectangle_area()
        elif self.shape_type == 'circle':
            return self._calculate_circle_area()
        else:
            raise ValueError("Unsupported shape type")

    def _calculate_rectangle_area(self):
        length = self.dimensions['length']
        width = self.dimensions['width']
        return length * width

    def _calculate_circle_area(self):
        radius = self.dimensions['radius']
        return math.pi * (radius ** 2)

if __name__ == '__main__':
    rectangle = Shape('rectangle', length=6, width=4)
    circle = Shape('circle', radius=5)

    print("Rectangle Area:", rectangle.area())
    print("Circle Area:", circle.area())