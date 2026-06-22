import math

class ShapeAreaCalculator:
    def __init__(self, shape):
        self.shape = shape

    def calculate(self):
        shape_type = self.shape.get('type')
        if shape_type == 'rectangle':
            width = self.shape.get('width')
            height = self.shape.get('height')
            return width * height
        elif shape_type == 'circle':
            radius = self.shape.get('radius')
            return math.pi * (radius ** 2)
        elif shape_type == 'triangle':
            base = self.shape.get('base')
            height = self.shape.get('height')
            return 0.5 * base * height
        else:
            raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    rectangle = ShapeAreaCalculator({'type': 'rectangle', 'width': 6, 'height': 12})
    circle = ShapeAreaCalculator({'type': 'circle', 'radius': 8})
    triangle = ShapeAreaCalculator({'type': 'triangle', 'base': 10, 'height': 5})

    print("Rectangle area:", rectangle.calculate())
    print("Circle area:", circle.calculate())
    print("Triangle area:", triangle.calculate())