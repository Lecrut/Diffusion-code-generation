import math

class Triangle:
    def __init__(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("Sides must be positive numbers")
        if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
            raise ValueError("Invalid triangle sides: does not satisfy triangle inequality theorem")
        self.sides = (side1, side2, side3)
    
    def get_sides(self):
        return self.sides

class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers")
        self.sides = (length, width, length, width)
    
    def get_sides(self):
        return self.sides

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        self.radius = radius
    
    def get_diameter(self):
        return 2 * self.radius

def measure_shapes(shapes):
    results = []
    for shape in shapes:
        try:
            sides = shape.get_sides()
            results.append((type(shape).__name__, sides))
        except AttributeError:
            raise ValueError("Shape does not have a get_sides method")
    return results

if __name__ == '__main__':
    triangle = Triangle(3, 4, 5)
    rectangle = Rectangle(2, 3)
    circle = Circle(1)

    shapes = [triangle, rectangle, circle]
    measurements = measure_shapes(shapes)
    for shape_name, sides in measurements:
        print(f"{shape_name}: {sides}")