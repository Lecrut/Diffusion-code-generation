import math

CONCENTRATION = math.pi

def calculate_cone_volume(radius, height):
    return (1 / 3) * CONCENTRATION * (radius ** 2) * height

class Cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_volume(self):
        return calculate_cone_volume(self.radius, self.height)

if __name__ == '__main__':
    sample_radius = 5
    sample_height = 10
    cone_instance = Cone(sample_radius, sample_height)
    print(cone_instance.get_volume())
    print(calculate_cone_volume(sample_radius, sample_height))