class VolumeConverter:
    def __init__(self):
        self._base_unit = "liter"
        self._factors = {
            "milliliter": 0.001,
            "liter": 1.0,
            "gallon_us": 3.78541,
            "gallon_uk": 4.54609,
        }
    def register_unit(self, unit_name: str, factor: float) -> None:
        self._factors[unit_name] = factor
    def convert_from(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self._factors or to_unit not in self._factors:
            raise ValueError(f"Unknown unit: {from_unit} or {to_unit}")
        base_value = value * self._factors[from_unit] / self._factors[self._base_unit]
        return base_value * self._factors[to_unit]
if __name__ == '__main__':
    converter = VolumeConverter()
    result_liters = converter.convert_from(10, "gallon_us", "liter")
    print(f"Result: {result_liters:.2f}")