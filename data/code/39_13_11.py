class PrismVolumeCalculator:
    BASE_AREA = 12.5
    HEIGHT = 8.0

    @staticmethod
    def compute_volume(base_area, height):
        return base_area * height

if __name__ == '__main__':
    volume = PrismVolumeCalculator.compute_volume(PrismVolumeCalculator.BASE_AREA, PrismVolumeCalculator.HEIGHT)
    print(volume)