import math

class Shape:
    SHAPE_TYPES = {
        'rectangle': 'calculate_rectangle_area',
        'circle': 'calculate_circle_area'
    }

    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions
        if self.shape_type not in self.SHAPE_TYPES:
            raise ValueError("Unsupported shape type")

    def area(self):
        method_name = self.SHAPE_TYPES[self.shape_type]
        return getattr(self, method_name)()

    @staticmethod
    def calculate_rectangle_area(length=0, width=0):
        return length * width

    @staticmethod
    def calculate_circle_area(radius=0):
        return math.pi * (radius ** 2)

if __name__ == '__main__':
    rectangle = Shape('rectangle', length=6, width=4)
    circle = Shape('circle', radius=5)
    
    print("Rectangle Area:", rectangle.area())
    print("Circle Area:", circle.area())