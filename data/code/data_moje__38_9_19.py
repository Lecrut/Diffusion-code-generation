import math

class ConeVolumeCalculator:
    PI = math.pi

    @staticmethod
    def calculate_volume(radius, height):
        base_area = ConeVolumeCalculator.PI * (radius ** 2)
        volume = (1 / 3) * base_area * height
        return volume

if __name__ == '__main__':
    calculator = ConeVolumeCalculator()
    computed_volume = calculator.calculate_volume(10, 20)
    print(computed_volume)