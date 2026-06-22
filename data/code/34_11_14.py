import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def calculate_lateral_surface_area(self):
        return 2 * math.pi * self.radius * self.height

    def calculate_total_surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

if __name__ == '__main__':
    sample_radius = 5.0
    sample_height = 10.0
    cylinder = Cylinder(sample_radius, sample_height)
    lateral_area = cylinder.calculate_lateral_surface_area()
    total_area = cylinder.calculate_total_surface_area()
    print(lateral_area)
    print(total_area)