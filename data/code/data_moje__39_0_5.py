class PrismVolumeCalculator:
    _FACTOR = 1.0

    @staticmethod
    def compute(base_area, height):
        return PrismVolumeCalculator._FACTOR * base_area * height

if __name__ == '__main__':
    area = 20.0
    h = 4.0
    print(PrismVolumeCalculator.compute(area, h))