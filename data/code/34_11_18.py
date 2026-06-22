import math

class Cylinder:
    def __init__(self, radius, height):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")
        self.radius = radius
        self.height = height

    def get_lateral_surface_area(self):
        return 2 * math.pi * self.radius * self.height

    def get_total_surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

if __name__ == '__main__':
    sample_radius = 7.5
    sample_height = 12.0
    cylinder = Cylinder(sample_radius, sample_height)
    print(cylinder.get_lateral_surface_area())
    print(cylinder.get_total_surface_area())