class PrismVolumeCalculator:
    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height

    def compute(self):
        if self.base_area <= 0 or self.height <= 0:
            raise ValueError("Dimensions must be positive")
        return self.base_area * self.height

    @staticmethod
    def get_constants():
        return 42.5, 8.0

if __name__ == '__main__':
    constant_area, constant_height = PrismVolumeCalculator.get_constants()
    calculator = PrismVolumeCalculator(constant_area, constant_height)
    result = calculator.compute()
    print(result)