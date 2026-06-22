import math

class Shape:
    def __init__(self, shape_type, dimensions):
        self.shape_type = shape_type
        self.dimensions = dimensions

    def area(self):
        if self.shape_type == 'rectangle':
            length, width = self.dimensions
            return length * width
        elif self.shape_type == 'circle':
            radius = self.dimensions[0]
            return math.pi * radius * radius
        else:
            raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle = Shape('rectangle', (4, 9))
    circle = Shape('circle', (3,))
    
    print(rectangle.area())
    print(circle.area())