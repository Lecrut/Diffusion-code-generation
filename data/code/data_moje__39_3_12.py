class PrismVolumeCalculator:
    def __init__(self, base_area: float, height: float) -> None:
        self.base_area = base_area
        self.height = height

    def get_volume(self) -> float:
        if self.base_area < 0:
            raise ValueError("Base area cannot be negative")
        if self.height < 0:
            raise ValueError("Height cannot be negative")
        return self.base_area * self.height

if __name__ == '__main__':
    test_area = 24.5
    test_height = 7.2
    calculator = PrismVolumeCalculator(test_area, test_height)
    print(calculator.get_volume())