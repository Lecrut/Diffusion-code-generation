class VolumeConverter:
    _BASE_UNIT = "liter"
    _FACTORS_TO_BASE = {
        "liter": 1.0,
        "milliliter": 0.001,
        "gallon_us": 3.785411784,
        "gallon_uk": 4.54609,
        "quart_us": 0.946352946,
        "quart_uk": 1.1365225,
        "pint_us": 0.473176473,
        "pint_uk": 0.56826125,
        "cup_us": 0.2365882365,
        "cup_uk": 0.284130625,
        "fluid_ounce_us": 0.0295735295625,
        "fluid_ounce_uk": 0.0284130625,
        "tablespoon_us": 0.01478676478125,
        "tablespoon_uk": 0.0177581640625,
        "teaspoon_us": 0.00492892159375,
        "teaspoon_uk": 0.005919388020833333,
        "cubic_meter": 1000.0,
        "cubic_decimeter": 1.0,
        "cubic_centimeter": 0.001,
        "cubic_inch": 0.016387064,
        "cubic_foot": 28.316846592,
        "barrel_oil": 158.987294928,
    }

    def __init__(self):
        self._inverse_factors = {unit: (1.0 / factor) for unit, factor in self._FACTORS_TO_BASE.items()}

    def to_base(self, value, unit):
        if unit not in self._FACTORS_TO_BASE:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self._FACTORS_TO_BASE[unit]

    def from_base(self, value, unit):
        if unit not in self._inverse_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self._inverse_factors[unit]

    def convert(self, value, source_unit, target_unit):
        base_value = self.to_base(value, source_unit)
        return self.from_base(base_value, target_unit)

if __name__ == "__main__":
    converter = VolumeConverter()
    liters = converter.to_base(5, "gallon_us")
    pints = converter.from_base(10, "liter")
    result = converter.convert(1, "gallon_uk", "fluid_ounce_us")
    print(liters)
    print(pints)
    print(result)