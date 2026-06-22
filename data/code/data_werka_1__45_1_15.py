import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    circle_attributes = {'radius': 3.0}
    circle_instance = Circle(circle_attributes['radius'])
    print(circle_instance.area())