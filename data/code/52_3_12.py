import math

class ShapeCalculator:
    def __init__(self, shape, *args):
        self.shape = shape.lower()
        self.args = args
        self.area = self._calculate_area()

    def _calculate_area(self):
        if self.shape == 'rectangle':
            length, width = self.args
            return length * width
        elif self.shape == 'circle':
            radius = self.args[0]
            return math.pi * (radius ** 2)
        elif self.shape == 'triangle':
            base, height = self.args
            return 0.5 * base * height
        else:
            raise ValueError("Unsupported shape")

    def get_area(self):
        return self.area

if __name__ == '__main__':
    rectangle = ShapeCalculator('rectangle', 5, 3)
    circle = ShapeCalculator('circle', 4)
    triangle = ShapeCalculator('triangle', 6, 2)

    print(rectangle.get_area())
    print(circle.get_area())
    print(triangle.get_area())