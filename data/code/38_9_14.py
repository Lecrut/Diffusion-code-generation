import math

class ConeCalculator:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def compute_volume(self):
        return (1 / 3) * math.pi * (self.radius ** 2) * self.height

    def get_dimensions(self):
        return self.radius, self.height

if __name__ == '__main__':
    sample_radius = 10
    sample_height = 20
    cone = ConeCalculator(sample_radius, sample_height)
    print(cone.compute_volume())
    print(cone.get_dimensions())