class VolumeConverter:
    BASE_UNIT = 'L'
    _CONVERSION_TO_BASE = {
        'L': 1.0,
        'mL': 0.001,
        'uL': 0.000001,
        'kL': 1000.0,
        'm3': 1000.0,
        'cm3': 0.001,
        'in3': 0.016387064,
        'ft3': 28.316846592,
        'gal': 3.785411784,
        'qt': 0.946352946,
        'pt': 0.473176473,
        'fl_oz': 0.0295735295625,
    }

    def __init__(self):
        self._conversion_from_base = {
            unit: (1.0 / factor) for unit, factor in self._CONVERSION_TO_BASE.items()
        }

    def to_base(self, value, from_unit):
        if from_unit not in self._CONVERSION_TO_BASE:
            raise ValueError(f"Unsupported unit: {from_unit}")
        factor = self._CONVERSION_TO_BASE[from_unit]
        return value * factor

    def from_base(self, value, to_unit):
        if to_unit not in self._conversion_from_base:
            raise ValueError(f"Unsupported unit: {to_unit}")
        factor = self._conversion_from_base[to_unit]
        return value * factor

    def convert(self, value, from_unit, to_unit):
        base_value = self.to_base(value, from_unit)
        return self.from_base(base_value, to_unit)

if __name__ == '__main__':
    converter = VolumeConverter()
    gallons_to_liters = converter.to_base(5, 'gal')
    liters_to_cubic_meters = converter.from_base(1000, 'm3')
    gallons_to_liters_back = converter.convert(1, 'gal', 'L')
    liters_to_gallons = converter.convert(3.785411784, 'L', 'gal')
    print(gallons_to_liters)
    print(liters_to_cubic_meters)
    print(gallons_to_liters_back)
    print(liters_to_gallons)