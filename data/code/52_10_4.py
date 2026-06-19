import math

class Shape:
    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions

    def area(self):
        if self.shape_type == 'rectangle':
            length = self.dimensions.get('length', 0)
            width = self.dimensions.get('width', 0)
            return length * width
        elif self.shape_type == 'circle':
            radius = self.dimensions.get('radius', 0)
            return math.pi * (radius ** 2)
        else:
            raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle = Shape('rectangle', length=5, width=3)
    circle = Shape('circle', radius=4)

    print("Rectangle area:", rectangle.area())
    print("Circle area:", circle.area())