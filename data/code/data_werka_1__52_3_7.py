import math

class ShapeAreaCalculator:
    def __init__(self, shape, *args):
        self.shape = shape
        self.args = args

    def calculate(self):
        if self.shape == 'rectangle':
            length, width = self.args
            return self._calculate_rectangle_area(length, width)
        elif self.shape == 'circle':
            radius = self.args[0]
            return self._calculate_circle_area(radius)
        elif self.shape == 'triangle':
            base, height = self.args
            return self._calculate_triangle_area(base, height)
        else:
            raise ValueError("Unsupported shape")

    def _calculate_rectangle_area(self, length, width):
        return length * width

    def _calculate_circle_area(self, radius):
        return math.pi * (radius ** 2)

    def _calculate_triangle_area(self, base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    rectangle = ShapeAreaCalculator('rectangle', 7, 4)
    circle = ShapeAreaCalculator('circle', 6)
    triangle = ShapeAreaCalculator('triangle', 8, 3)

    print(rectangle.calculate())
    print(circle.calculate())
    print(triangle.calculate())