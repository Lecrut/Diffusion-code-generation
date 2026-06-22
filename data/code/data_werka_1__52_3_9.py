import math

class Shape:
    def __init__(self, shape_type, *dimensions):
        self.shape_type = shape_type
        self.dimensions = dimensions

    def calculate_area(self):
        if self.shape_type == 'rectangle':
            length, width = self.dimensions
            return length * width
        elif self.shape_type == 'circle':
            radius = self.dimensions[0]
            return math.pi * (radius ** 2)
        elif self.shape_type == 'triangle':
            base, height = self.dimensions
            return 0.5 * base * height
        else:
            raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle = Shape('rectangle', 5, 3)
    circle = Shape('circle', 4)
    triangle = Shape('triangle', 6, 2)

    print(rectangle.calculate_area())
    print(circle.calculate_area())
    print(triangle.calculate_area())