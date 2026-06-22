import math

class ConeVolumeCalculator:
    ONE_THIRD = 1 / 3

    @staticmethod
    def calculate(radius: float, height: float) -> float:
        base_area = math.pi * (radius ** 2)
        return base_area * height * ConeVolumeCalculator.ONE_THIRD

if __name__ == '__main__':
    radius_value = 6
    height_value = 9
    cone_calculator = ConeVolumeCalculator()
    final_volume = cone_calculator.calculate(radius_value, height_value)
    print(final_volume)