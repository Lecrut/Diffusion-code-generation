import math
class VolumeConverter:
    def __init__(self):
        self._base_unit = "liter"
        self._factors = {
            "liter": 1.0,
            "milliliter": 0.001,
            "gallon_us": 3.78541,
            "cubic_meter": 1000.0,
            "fluid_ounce_us": 29.5735
        }
    def register_unit(self, unit_name: str, factor: float) -> None:
        self._factors[unit_name] = factor
    def convert_from(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self._factors or to_unit not in self._factors:
            raise ValueError(f"Unknown unit: {from_unit} or {to_unit}")
        base_value = value * self._factors[from_unit] / self._factors[self._base_unit]
        return base_value * self._factors[to_unit]
    def get_available_units(self) -> list[str]:
        return list(self._factors.keys())
if __name__ == '__main__':
    converter = VolumeConverter()
    converter.register_unit("barrel_oil", 158.9872)
    sample_value = 10.0
    result_liters = converter.convert_from(sample_value, "gallon_us", "liter")
    result_barrels = converter.convert_from(sample_value, "gallon_us", "barrel_oil")
    print(f"{sample_value} gallons (US) is {result_liters:.4f} liters.")
    print(f"{sample_value} gallons (US) is {result_barrels:.6f} barrels of oil.")