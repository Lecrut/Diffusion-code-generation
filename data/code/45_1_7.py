import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    circle_properties = {'radius': 3.0}
    circle_instance = Circle(circle_properties['radius'])
    print(circle_instance.area())