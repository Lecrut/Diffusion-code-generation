import math

class VolumeCalculator:
    CUBE_EDGE_LENGTH = 3
    SPHERE_RADIUS = 2

    @staticmethod
    def calculate_cube_volume(edge_length):
        return edge_length ** 3

    @staticmethod
    def calculate_sphere_volume(radius):
        return (4/3) * math.pi * (radius ** 3)

    @classmethod
    def is_cube_volume_greater(cls):
        cube_volume = cls.calculate_cube_volume(cls.CUBE_EDGE_LENGTH)
        sphere_volume = cls.calculate_sphere_volume(cls.SPHERE_RADIUS)
        return cube_volume > sphere_volume

if __name__ == '__main__':
    result = VolumeCalculator.is_cube_volume_greater()
    print(result)