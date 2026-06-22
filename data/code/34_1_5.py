import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_radius(self):
        return self.radius

    def get_height(self):
        return self.height

    def surface_area(self):
        side = 2 * math.pi * self.radius * self.height
        top_bottom = 2 * math.pi * self.radius * self.radius
        return side + top_bottom

if __name__ == '__main__':
    shape = Cylinder(7, 14)
    print(shape.get_radius())
    print(shape.get_height())
    print(shape.surface_area())