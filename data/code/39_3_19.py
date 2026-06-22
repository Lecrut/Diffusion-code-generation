class PrismVolumeCalculator:
    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height

    def calculate_volume(self):
        return self.base_area * self.height

if __name__ == '__main__':
    sample_base_area = 50.0
    sample_height = 12.5
    calculator = PrismVolumeCalculator(sample_base_area, sample_height)
    print(calculator.calculate_volume())