class PrismVolumeCalculator:
    BASE_AREA = 125.5
    HEIGHT = 8.2

    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height

    def calculate(self):
        return self.base_area * self.height

if __name__ == '__main__':
    calculator = PrismVolumeCalculator(125.5, 8.2)
    final_volume = calculator.calculate()
    print(final_volume)