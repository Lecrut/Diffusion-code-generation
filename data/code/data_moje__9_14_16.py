class VolumeConverter:
    UNIT_NAMES = ['liters', 'milliliters', 'gallons', 'quarts', 'pints', 'cups', 'fluid_ounces']

    CONVERSION_TO_LITERS = {
        'liters': 1.0,
        'milliliters': 0.001,
        'gallons': 3.785411784,
        'quarts': 0.946352946,
        'pints': 0.473176473,
        'cups': 0.2365882365,
        'fluid_ounces': 0.02957352956
    }

    def __init__(self):
        self._conversion_cache = {}

    def _normalize_unit_name(self, unit):
        unit_lower = unit.lower().strip()
        if unit_lower == 'ml':
            return 'milliliters'
        if unit_lower == 'l':
            return 'liters'
        if unit_lower == 'gal':
            return 'gallons'
        if unit_lower == 'qt':
            return 'quarts'
        if unit_lower == 'pt':
            return 'pints'
        if unit_lower == 'cup':
            return 'cups'
        if unit_lower == 'fl_oz' or unit_lower == 'floz':
            return 'fluid_ounces'
        return unit_lower

    def _validate_unit(self, unit):
        normalized = self._normalize_unit_name(unit)
        if normalized not in self.CONVERSION_TO_LITERS:
            raise ValueError(f"Unsupported unit: {unit}")
        return normalized

    def convert(self, value, from_unit, to_unit):
        from_norm = self._validate_unit(from_unit)
        to_norm = self._validate_unit(to_unit)

        if from_norm == to_norm:
            return value

        value_in_liters = value * self.CONVERSION_TO_LITERS[from_norm]
        result = value_in_liters / self.CONVERSION_TO_LITERS[to_norm]
        return result

    def convert_multiple(self, values_and_units, to_unit):
        to_norm = self._validate_unit(to_unit)
        results = []
        for value, unit in values_and_units:
            result = self.convert(value, unit, to_norm)
            results.append(result)
        return results

    def get_supported_units(self):
        return list(self.UNIT_NAMES)

if __name__ == '__main__':
    converter = VolumeConverter()

    liters_to_ml = converter.convert(1.0, 'liters', 'milliliters')
    print(liters_to_ml)

    gallons_to_liters = converter.convert(1.0, 'gallons', 'liters')
    print(gallons_to_liters)

    pints_to_cups = converter.convert(2.0, 'pints', 'cups')
    print(pints_to_cups)

    fl_oz_to_ml = converter.convert(8.0, 'fluid_ounces', 'milliliters')
    print(fl_oz_to_ml)

    quarts_to_gallons = converter.convert(4.0, 'quarts', 'gallons')
    print(quarts_to_gallons)

    mixed_conversions = converter.convert_multiple(
        [(1.0, 'liters'), (1.0, 'gallons'), (16.0, 'fluid_ounces')],
        'milliliters'
    )
    print(mixed_conversions)

    print(converter.get_supported_units())