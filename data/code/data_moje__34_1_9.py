import math

class Cylinder:
    def __init__(self, radius, height):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")
        self.radius = float(radius)
        self.height = float(height)

    def surface_area(self):
        base_area = self._calculate_base_area()
        lateral_area = self._calculate_lateral_area()
        return (2 * base_area) + lateral_area

    def _calculate_base_area(self):
        return math.pi * self.radius ** 2

    def _calculate_lateral_area(self):
        return 2 * math.pi * self.radius * self.height

if __name__ == '__main__':
    test_cylinder = Cylinder(7, 12)
    area_value = test_cylinder.surface_area()
    print(area_value)