import math

CONE_VOLUME_CONSTANT = 1.0 / 3.0

class GeometricCone:
    def __init__(self, radius, height):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")
        self.radius = radius
        self.height = height

    def compute_volume(self):
        area_base = math.pi * (self.radius ** 2)
        return CONE_VOLUME_CONSTANT * area_base * self.height

if __name__ == '__main__':
    r_sample = 3.0
    h_sample = 7.0
    cone_instance = GeometricCone(r_sample, h_sample)
    volume_output = cone_instance.compute_volume()
    print(volume_output)