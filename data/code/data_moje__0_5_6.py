class UnitConverter:
    def __init__(self):
        self._base_unit = 'meters'
        self._factors = {}
        self._register_default_units()

    def _register_default_units(self):
        factors = {
            'meters': 1.0,
            'kilometers': 1000.0,
            'centimeters': 0.01,
            'millimeters': 0.001,
            'miles': 1609.34,
            'yards': 0.9144,
            'feet': 0.3048,
            'inches': 0.0254
        }
        for unit, factor in factors.items():
            self.register_unit(unit, factor)

    def register_unit(self, unit_name, factor_to_base):
        self._factors[unit_name.lower()] = float(factor_to_base)

    def convert(self, value, from_unit, to_unit):
        from_key = from_unit.lower()
        to_key = to_unit.lower()

        if from_key not in self._factors:
            raise ValueError(f"Unknown source unit: {from_unit}")
        if to_key not in self._factors:
            raise ValueError(f"Unknown target unit: {to_unit}")

        value_in_base = value * self._factors[from_key]
        result = value_in_base / self._factors[to_key]
        return result

def convert_units(value, from_unit, to_unit):
    converter = UnitConverter()
    return converter.convert(value, from_unit, to_unit)

if __name__ == '__main__':
    result1 = convert_units(1.0, 'kilometers', 'meters')
    print(result1)

    result2 = convert_units(5280.0, 'feet', 'miles')
    print(result2)

    result3 = convert_units(100.0, 'centimeters', 'inches')
    print(result3)

    converter = UnitConverter()
    converter.register_unit('light_year', 9.461e15)
    result4 = converter.convert(1.0, 'light_year', 'meters')
    print(result4)