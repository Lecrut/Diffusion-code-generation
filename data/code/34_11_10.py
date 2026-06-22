class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def lateral_surface_area(self):
        return 2 * 3.141592653589793 * self.radius * self.height

    def total_surface_area(self):
        return 2 * 3.141592653589793 * self.radius * (self.radius + self.height)

if __name__ == '__main__':
    sample_radius = 5
    sample_height = 10
    cylinder = Cylinder(sample_radius, sample_height)
    print(cylinder.lateral_surface_area())
    print(cylinder.total_surface_area())