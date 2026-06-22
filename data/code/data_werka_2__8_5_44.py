import math

class ShapeCalculator:
    def __init__(self, shape):
        self.shape = shape

    def calculate_area(self):
        shape_type = self.shape.get('type')
        if shape_type == 'rectangle':
            return self._calculate_rectangle_area()
        elif shape_type == 'circle':
            return self._calculate_circle_area()
        elif shape_type == 'triangle':
            return self._calculate_triangle_area()
        else:
            raise ValueError(f"Unsupported shape type: {shape_type}")

    def _calculate_rectangle_area(self):
        width = self.shape.get('width')
        height = self.shape.get('height')
        if width is None or height is None:
            raise ValueError("Width and height are required for rectangle")
        return width * height

    def _calculate_circle_area(self):
        radius = self.shape.get('radius')
        if radius is None:
            raise ValueError("Radius is required for circle")
        return math.pi * (radius ** 2)

    def _calculate_triangle_area(self):
        base = self.shape.get('base')
        height = self.shape.get('height')
        if base is None or height is None:
            raise ValueError("Base and height are required for triangle")
        return 0.5 * base * height

if __name__ == '__main__':
    rectangle = {'type': 'rectangle', 'width': 5, 'height': 10}
    circle = {'type': 'circle', 'radius': 7}
    triangle = {'type': 'triangle', 'base': 8, 'height': 6}

    calculator = ShapeCalculator(rectangle)
    print("Rectangle area:", calculator.calculate_area())

    calculator.shape = circle
    print("Circle area:", calculator.calculate_area())

    calculator.shape = triangle
    print("Triangle area:", calculator.calculate_area())