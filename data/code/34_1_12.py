import math

TWO_PI = 2.0 * math.pi

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def _base_area(self):
        return math.pi * self.radius * self.radius

    def _lateral_area(self):
        return TWO_PI * self.radius * self.height

    def surface_area(self):
        return 2 * self._base_area() + self._lateral_area()

if __name__ == '__main__':
    sample_cylinder = Cylinder(7.0, 12.0)
    computed_area = sample_cylinder.surface_area()
    print(computed_area)