import math

class Shape:
    SHAPE_TYPES = ['rectangle', 'circle']
    
    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type.lower()
        if self.shape_type not in Shape.SHAPE_TYPES:
            raise ValueError("Unsupported shape type")
        self.dimensions = dimensions
        self._validate_dimensions()

    def _validate_dimensions(self):
        if self.shape_type == 'rectangle':
            if 'length' not in self.dimensions or 'width' not in self.dimensions:
                raise ValueError("Rectangle requires 'length' and 'width'")
        elif self.shape_type == 'circle':
            if 'radius' not in self.dimensions:
                raise ValueError("Circle requires 'radius'")

    def area(self):
        return Shape._calculate_area(self.shape_type, self.dimensions)

    @staticmethod
    def _calculate_area(shape_type, dimensions):
        if shape_type == 'rectangle':
            length = dimensions['length']
            width = dimensions['width']
            return length * width
        elif shape_type == 'circle':
            radius = dimensions['radius']
            return math.pi * (radius ** 2)

if __name__ == '__main__':
    rectangle = Shape('rectangle', length=6, width=4)
    circle = Shape('circle', radius=5)
    
    print("Rectangle Area:", rectangle.area())
    print("Circle Area:", circle.area())