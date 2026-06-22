class PrismVolumeCalculator:
    def __init__(self, base_area: float, height: float) -> None:
        if not isinstance(base_area, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("base_area and height must be numeric types")
        if base_area <= 0 or height <= 0:
            raise ValueError("base_area and height must be positive numbers")
        self.base_area = base_area
        self.height = height

    def calculate_volume(self) -> float:
        return self.base_area * self.height

if __name__ == "__main__":
    base_area_value = 25.5
    height_value = 10.0
    calculator = PrismVolumeCalculator(base_area_value, height_value)
    result = calculator.calculate_volume()
    print(result)