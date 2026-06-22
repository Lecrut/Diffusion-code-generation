import math

class Cylinder:
    PI = math.pi

    def __init__(self, radius, height):
        if radius <= 0 or height <= 0:
            raise ValueError("Radius and height must be positive")
        self.radius = radius
        self.height = height

    def _compute_lateral_area(self):
        return 2 * self.PI * self.radius * self.height

    def _compute_base_area(self):
        return self.PI * self.radius ** 2

    def surface_area(self):
        return 2 * self._compute_base_area() + self._compute_lateral_area()

if __name__ == '__main__':
    test_cylinder = Cylinder(7.5, 12.0)
    area = test_cylinder.surface_area()
    print(area)