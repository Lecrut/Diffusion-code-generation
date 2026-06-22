import math

class ConeVolumeCalculator:
    PI = math.pi
    FACTOR = 1 / 3

    @staticmethod
    def compute_volume(radius, height):
        base_area = ConeVolumeCalculator.PI * radius ** 2
        return ConeVolumeCalculator.FACTOR * base_area * height

if __name__ == '__main__':
    radius_value = 6
    height_value = 9
    calculated_volume = ConeVolumeCalculator.compute_volume(radius_value, height_value)
    print(calculated_volume)