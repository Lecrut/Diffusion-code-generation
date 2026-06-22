class VolumeConverter:
    def __init__(self):
        self._factors = {
            'liter': 1.0,
            'milliliter': 0.001,
            'cubic_meter': 1000.0,
            'gallon': 3.78541,
            'quart': 0.946353,
            'pint': 0.473176,
            'cup': 0.236588,
            'fluid_ounce': 0.0295735,
            'tablespoon': 0.0147868,
            'teaspoon': 0.00492892
        }
        self._base_unit = 'liter'

    def to_base(self, value, unit):
        unit = unit.lower()
        if unit not in self._factors:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self._factors[unit]

    def from_base(self, value, unit):
        unit = unit.lower()
        if unit not in self._factors:
            raise ValueError(f"Unsupported unit: {unit}")
        return value / self._factors[unit]

    def convert(self, value, from_unit, to_unit):
        base_value = self.to_base(value, from_unit)
        return self.from_base(base_value, to_unit)

if __name__ == '__main__':
    converter = VolumeConverter()
    result = converter.convert(1.0, 'gallon', 'liter')
    print(result)
    
    result2 = converter.convert(500, 'milliliter', 'cup')
    print(result2)
    
    result3 = converter.convert(10, 'liter', 'gallon')
    print(result3)