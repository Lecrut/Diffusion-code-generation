import math

class ShapeCalculator:
    def __init__(self, shape):
        self.shape = shape

    def calculate_area(self):
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
    rectangle = {'type': 'rectangle', 'width': 6, 'height': 12}
    circle = {'type': 'circle', 'radius': 8}
    triangle = {'type': 'triangle', 'base': 10, 'height': 5}

    calculator = ShapeCalculator(rectangle)
    print("Rectangle area:", calculator.calculate_area())

    calculator.shape = circle
    print("Circle area:", calculator.calculate_area())

    calculator.shape = triangle
    print("Triangle area:", calculator.calculate_area())