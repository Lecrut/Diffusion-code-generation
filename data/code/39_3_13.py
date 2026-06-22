class PrismVolumeCalculator:
    VOLUME_MULTIPLIER = 1.0

    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height

    def compute(self):
        if self.base_area < 0 or self.height < 0:
            raise ValueError("Dimensions must be non-negative")
        return self.base_area * self.height * self.VOLUME_MULTIPLIER

    @staticmethod
    def validate_dimension(value, name):
        if value < 0:
            raise ValueError(f"{name} cannot be negative")
        return True

if __name__ == '__main__':
    calc_area = 24.5
    calc_height = 7.2
    PrismVolumeCalculator.validate_dimension(calc_area, "Base Area")
    PrismVolumeCalculator.validate_dimension(calc_height, "Height")
    calculator = PrismVolumeCalculator(calc_area, calc_height)
    print(calculator.compute())