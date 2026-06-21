class VolumeConverter:
    def __init__(self):
        self._units = {
            'liter': 1.0,
            'milliliter': 0.001,
            'gallon': 3.785411784,
            'quart': 0.946352946,
            'pint': 0.473176473,
            'cup': 0.2365882365,
            'fluid_ounce': 0.0295735295625,
            'tablespoon': 0.01478676478125,
            'teaspoon': 0.00492892159375,
            'cubic_meter': 1000.0,
            'cubic_centimeter': 0.001,
            'cubic_inch': 0.016387064,
            'cubic_foot': 28.316846592,
            'imperial_gallon': 4.54609,
            'imperial_pint': 0.56826125,
        }
        self._base_unit = 'liter'

    def to_base(self, value, from_unit):
        if from_unit not in self._units:
            raise ValueError(f"Unsupported unit: {from_unit}")
        return value * self._units[from_unit]

    def from_base(self, value, to_unit):
        if to_unit not in self._units:
            raise ValueError(f"Unsupported unit: {to_unit}")
        return value / self._units[to_unit]

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self._units:
            raise ValueError(f"Unsupported unit: {from_unit}")
        if to_unit not in self._units:
            raise ValueError(f"Unsupported unit: {to_unit}")
        base_value = self.to_base(value, from_unit)
        return self.from_base(base_value, to_unit)

if __name__ == '__main__':
    converter = VolumeConverter()
    result = converter.convert(1, 'gallon', 'liter')
    print(result)
    result2 = converter.convert(1000, 'milliliter', 'gallon')
    print(result2)