import math

SHAPE_TYPES = {
    'rectangle': lambda length, width: length * width,
    'circle': lambda radius: math.pi * (radius ** 2)
}

class Shape:
    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions

    def area(self):
        if self.shape_type in SHAPE_TYPES:
            calc_function = SHAPE_TYPES[self.shape_type]
            return calc_function(**self.dimensions)
        else:
            raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle = Shape('rectangle', length=7, width=2)
    circle = Shape('circle', radius=3)

    print(f"Rectangle area: {rectangle.area()}")
    print(f"Circle area: {circle.area()}")