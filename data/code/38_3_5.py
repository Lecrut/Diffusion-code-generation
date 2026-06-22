import math

class ConeVolumeCalculator:
    PI = math.pi
    FACTOR = 1 / 3

    @staticmethod
    def _base_area(radius):
        return ConeVolumeCalculator.PI * radius ** 2

    @classmethod
    def compute(cls, radius, height):
        return cls.FACTOR * cls._base_area(radius) * height

def calculate_cone_volume(radius, height):
    return ConeVolumeCalculator.compute(radius, height)

if __name__ == '__main__':
    volume = calculate_cone_volume(4, 12)
    print(volume)