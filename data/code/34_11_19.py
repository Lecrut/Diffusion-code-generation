import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self._circumference = 2 * math.pi * radius
        self._base_area = math.pi * (self.radius ** 2)

    def lateral_surface_area(self):
        return self._circumference * self.height

    def total_surface_area(self):
        return self.lateral_surface_area() + (2 * self._base_area)

if __name__ == '__main__':
    cyl = Cylinder(5.0, 10.0)
    print(cyl.lateral_surface_area())
    print(cyl.total_surface_area())