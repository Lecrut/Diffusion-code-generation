class VolumeConverter:
    _BASE_UNIT = "liter"
    _FACTORS_TO_BASE = {
        "liter": 1.0,
        "litre": 1.0,
        "milliliter": 0.001,
        "millilitre": 0.001,
        "cubic_meter": 1000.0,
        "cubic_decimeter": 1.0,
        "cubic_centimeter": 0.001,
        "cubic_inch": 0.016387064,
        "cubic_foot": 28.316846592,
        "cubic_yard": 764.554857984,
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
        "barrel_oil": 158.987294928,
        "barrel_us": 119.240471196,
    }

    def __init__(self):
        self._cache = {}

    def _get_factor(self, unit):
        normalized = unit.lower().strip()
        if normalized in self._FACTORS_TO_BASE:
            return self._FACTORS_TO_BASE[normalized]
        raise ValueError(f"Unsupported unit: {unit}")

    def to_base(self, value, from_unit):
        if from_unit in self._cache:
            factor = self._cache[from_unit]
        else:
            factor = self._get_factor(from_unit)
            self._cache[from_unit] = factor
        return value * factor

    def from_base(self, value, to_unit):
        if to_unit in self._cache:
            factor = self._cache[to_unit]
        else:
            factor = self._get_factor(to_unit)
            self._cache[to_unit] = factor
        return value / factor

    def convert(self, value, from_unit, to_unit):
        base_value = self.to_base(value, from_unit)
        return self.from_base(base_value, to_unit)

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_value = 100.0
    source_unit = "gallon_us"
    target_unit = "liter"
    result_liters = converter.to_base(sample_value, source_unit)
    back_to_gallons = converter.from_base(result_liters, source_unit)
    direct_convert = converter.convert(sample_value, source_unit, "cubic_meter")
    print(f"{sample_value} {source_unit} = {result_liters} {target_unit}")
    print(f"{result_liters} {target_unit} = {back_to_gallons} {source_unit}")
    print(f"{sample_value} {source_unit} = {direct_convert} cubic_meter")