import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        pi_value = math.pi
        radius_sq = self.radius * self.radius
        base_contribution = pi_value * radius_sq
        lateral_contribution = 2 * pi_value * self.radius * self.height
        total_area = 2 * base_contribution + lateral_contribution
        return total_area

if __name__ == '__main__':
    sample_radius = 7.5
    sample_height = 12.0
    cyl = Cylinder(sample_radius, sample_height)
    computed_area = cyl.surface_area()
    print(computed_area)