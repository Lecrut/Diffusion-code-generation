import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def get_sides(self):
        return (self.side1, self.side2, self.side3)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def get_sides(self):
        return (self.length, self.width, self.length, self.width)

class Circle:
    PI = math.pi
    
    def __init__(self, radius):
        self.radius = radius
    
    def get_diameter(self):
        return 2 * self.radius
    
    def get_side_length(self):
        return self.get_diameter()

def measure_shapes(shapes):
    results = []
    for shape in shapes:
        if hasattr(shape, 'get_sides'):
            sides = shape.get_sides()
        elif isinstance(shape, Circle):
            sides = (shape.get_side_length(),)
        else:
            raise ValueError(f"Unsupported shape type: {type(shape)}")
        results.append(sides)
    return results

if __name__ == '__main__':
    triangle = Triangle(3, 4, 5)
    rectangle = Rectangle(6, 8)
    circle = Circle(7)

    shapes = [triangle, rectangle, circle]
    side_lengths = measure_shapes(shapes)
    for sides in side_lengths:
        print(sides)