class VolumeConverter:
    def __init__(self):
        self._factors_to_liters = {
            'liters': 1.0,
            'milliliters': 0.001,
            'gallons': 3.785411784,
            'quarts': 0.946352946,
            'pints': 0.473176473,
            'cups': 0.2365882365,
            'fluid_ounces': 0.0295735295625
        }

    def _to_liters(self, value, unit):
        unit_lower = unit.lower()
        if unit_lower not in self._factors_to_liters:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self._factors_to_liters[unit_lower]

    def _from_liters(self, value_liters, unit):
        unit_lower = unit.lower()
        if unit_lower not in self._factors_to_liters:
            raise ValueError(f"Unsupported unit: {unit}")
        factor = self._factors_to_liters[unit_lower]
        if factor == 0:
            raise ValueError("Conversion factor is zero")
        return value_liters / factor

    def convert(self, value, from_unit, to_unit):
        liters = self._to_liters(value, from_unit)
        return self._from_liters(liters, to_unit)

if __name__ == '__main__':
    converter = VolumeConverter()
    result = converter.convert(1.0, 'gallons', 'liters')
    print(result)
    result2 = converter.convert(1.0, 'liters', 'milliliters')
    print(result2)
    result3 = converter.convert(8.0, 'fluid_ounces', 'cups')
    print(result3)