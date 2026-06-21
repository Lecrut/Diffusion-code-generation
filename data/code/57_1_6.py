import math

class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()

    def calculate_area(self, *args):
        if self.shape_type == 'circle':
            return self._calculate_circle_area(args[0])
        elif self.shape_type == 'rectangle':
            return self._calculate_rectangle_area(args[0], args[1])
        else:
            raise ValueError("Unsupported shape type")

    def _calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def _calculate_rectangle_area(self, length, width):
        return length * width

if __name__ == '__main__':
    circle = Shape('circle')
    rectangle = Shape('rectangle')

    circle_radius = 5.0
    rectangle_length = 4.0
    rectangle_width = 6.0

    print(circle.calculate_area(circle_radius))
    print(rectangle.calculate_area(rectangle_length, rectangle_width))