import math

CIRCULAR_SHAPE_AREA_CONST = 3.14

class CircularShape:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return CIRCULAR_SHAPE_AREA_CONST * self.radius ** 2

def circular_shape_generator(radius, iterations):
    for _ in range(iterations):
        yield CircularShape(radius)

if __name__ == '__main__':
    generator = circular_shape_generator(5, 3)
    for shape in generator:
        print(shape.area())