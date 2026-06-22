import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    circle_definitions = [
        {'radius': 3},
        {'radius': 8}
    ]
    
    for definition in circle_definitions:
        circle = Circle(definition['radius'])
        print(circle.perimeter())