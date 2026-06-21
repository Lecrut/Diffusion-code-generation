class VolumeConverter:
    _TO_LITER = {
        'liter': 1.0,
        'milliliter': 0.001,
        'gallon_us': 3.785411784,
        'gallon_uk': 4.54609,
        'quart_us': 0.946352946,
        'quart_uk': 1.1365225,
        'pint_us': 0.473176473,
        'pint_uk': 0.56826125,
        'cup_us': 0.24,
        'fluid_ounce_us': 0.0295735295625,
        'fluid_ounce_uk': 0.0284130625,
        'tablespoon_us': 0.01478676478125,
        'teaspoon_us': 0.00492892159375,
        'cubic_meter': 1000.0,
        'cubic_foot': 28.316846592,
        'cubic_inch': 0.016387064,
        'barrel_oil': 158.987294928,
    }

    def __init__(self):
        self._base_unit = 'liter'

    def to_base(self, value, unit):
        if unit not in self._TO_LITER:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self._TO_LITER[unit]

    def from_base(self, value, unit):
        if unit not in self._TO_LITER:
            raise ValueError(f"Unsupported unit: {unit}")
        factor = self._TO_LITER[unit]
        return value / factor

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self._TO_LITER or to_unit not in self._TO_LITER:
            raise ValueError("Unsupported unit provided")
        liters = value * self._TO_LITER[from_unit]
        return liters / self._TO_LITER[to_unit]

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_volume = 5.0
    source_unit = 'gallon_us'
    target_unit = 'liter'
    result = converter.convert(sample_volume, source_unit, target_unit)
    print(result)
    base_val = converter.to_base(sample_volume, source_unit)
    back_to_original = converter.from_base(base_val, source_unit)
    print(back_to_original)
    cubic_meters = converter.convert(1000.0, 'liter', 'cubic_meter')
    print(cubic_meters)