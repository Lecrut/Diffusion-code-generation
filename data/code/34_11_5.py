class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_lateral_surface_area(self):
        return 2 * 3.141592653589793 * self.radius * self.height

    def get_total_surface_area(self):
        lateral_area = self.get_lateral_surface_area()
        base_area = 3.141592653589793 * self.radius * self.radius
        return lateral_area + 2 * base_area

if __name__ == '__main__':
    sample_radius = 5
    sample_height = 10
    cylinder = Cylinder(sample_radius, sample_height)
    print(cylinder.get_lateral_surface_area())
    print(cylinder.get_total_surface_area())