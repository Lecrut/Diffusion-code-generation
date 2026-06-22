import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = (side1, side2, side3)
    
    def get_sides(self):
        return self.sides

class Rectangle:
    def __init__(self, length, width):
        self.sides = (length, width, length, width)
    
    def get_sides(self):
        return self.sides

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_diameter(self):
        return 2 * self.radius

def measure_shapes(shapes):
    results = []
    for shape in shapes:
        if isinstance(shape, Triangle):
            results.append(('Triangle', shape.get_sides()))
        elif isinstance(shape, Rectangle):
            results.append(('Rectangle', shape.get_sides()))
        elif isinstance(shape, Circle):
            results.append(('Circle', (shape.get_diameter(),)))
        else:
            raise ValueError("Unsupported shape type")
    return results

if __name__ == '__main__':
    triangle = Triangle(3, 4, 5)
    rectangle = Rectangle(6, 8)
    circle = Circle(10)

    shapes = [triangle, rectangle, circle]
    measurements = measure_shapes(shapes)

    for shape_name, sides in measurements:
        print(f"{shape_name}: {sides}")