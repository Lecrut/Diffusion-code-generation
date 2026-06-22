import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

if __name__ == '__main__':
    cylinder = Cylinder(3.0, 5.0)
    result = cylinder.surface_area()
    print(result)