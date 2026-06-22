import math

UNIT_MULTIPLIERS = {
    'mm': 0.001,
    'cm': 0.01,
    'm': 1.0,
    'km': 1000.0,
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144
}

class Cylinder:
    def __init__(self, radius, height, unit='m'):
        self.radius = radius
        self.height = height
        multiplier = UNIT_MULTIPLIERS.get(unit, 1.0)
        self._radius_m = radius * multiplier
        self._height_m = height * multiplier

    def surface_area(self):
        base_part = 2 * math.pi * self._radius_m ** 2
        side_part = 2 * math.pi * self._radius_m * self._height_m
        return base_part + side_part

if __name__ == '__main__':
    test_cylinder = Cylinder(radius=15, height=25, unit='cm')
    print(test_cylinder.surface_area())