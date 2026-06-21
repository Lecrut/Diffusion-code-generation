import math

class Triangle:
    def __init__(self, side1, side2, side3):
        if not self._is_valid_triangle(side1, side2, side3):
            raise ValueError("Invalid triangle sides")
        self.sides = (side1, side2, side3)

    def get_sides(self):
        return self.sides

    @staticmethod
    def _is_valid_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive")
        self.sides = (length, width, length, width)

    def get_sides(self):
        return self.sides

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def get_diameter(self):
        return 2 * self.radius

def measure_shapes(shapes):
    results = []
    for shape in shapes:
        if isinstance(shape, Triangle):
            sides = shape.get_sides()
        elif isinstance(shape, Rectangle):
            sides = shape.get_sides()
        elif isinstance(shape, Circle):
            diameter = shape.get_diameter()
            sides = (diameter,)
        else:
            raise ValueError("Unsupported shape type")
        results.append((shape.__class__.__name__, sides))
    return results

if __name__ == '__main__':
    triangle = Triangle(3, 4, 5)
    rectangle = Rectangle(6, 8)
    circle = Circle(10)

    shapes = [triangle, rectangle, circle]
    measurements = measure_shapes(shapes)

    for shape_name, sides in measurements:
        print(f"{shape_name}: {sides}")