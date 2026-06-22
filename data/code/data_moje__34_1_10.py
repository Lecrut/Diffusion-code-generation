import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        base_area = math.pi * self.radius ** 2
        side_area = 2 * math.pi * self.radius * self.height
        return 2 * base_area + side_area

if __name__ == '__main__':
    c = Cylinder(5, 10)
    print(c.surface_area())