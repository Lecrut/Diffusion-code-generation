class VolumeConverter:
    UNIT_TO_LITER_FACTOR = {
        'liter': 1.0,
        'liters': 1.0,
        'ml': 0.001,
        'milliliters': 0.001,
        'gallon': 3.785411784,
        'gallons': 3.785411784,
        'quart': 0.946352946,
        'quarts': 0.946352946,
        'pint': 0.473176473,
        'pints': 0.473176473,
        'cup': 0.2365882365,
        'cups': 0.2365882365,
        'fluid_ounce': 0.0295735295625,
        'fluid_ounces': 0.0295735295625,
        'floz': 0.0295735295625
    }

    def __init__(self):
        self._factors = dict(VolumeConverter.UNIT_TO_LITER_FACTOR)

    def _normalize_unit(self, unit):
        normalized = unit.strip().lower()
        return normalized if normalized in self._factors else None

    def _to_liters(self, value, unit):
        factor = self._factors[unit]
        return value * factor

    def _from_liters(self, liters, unit):
        factor = self._factors[unit]
        return liters / factor

    def convert(self, value, from_unit, to_unit):
        normalized_from = self._normalize_unit(from_unit)
        normalized_to = self._normalize_unit(to_unit)

        if normalized_from is None:
            raise ValueError("Invalid source unit: " + str(from_unit))
        if normalized_to is None:
            raise ValueError("Invalid target unit: " + str(to_unit))

        liters = self._to_liters(value, normalized_from)
        return self._from_liters(liters, normalized_to)

    def batch_convert(self, values_with_units, to_unit):
        results = []
        for item in values_with_units:
            val, unit = item
            converted = self.convert(val, unit, to_unit)
            results.append(converted)
        return results

    def get_supported_units(self):
        return list(self._factors.keys())

    def reverse_convert(self, target_value, to_unit, from_unit):
        normalized_to = self._normalize_unit(to_unit)
        normalized_from = self._normalize_unit(from_unit)

        if normalized_to is None:
            raise ValueError("Invalid target unit: " + str(to_unit))
        if normalized_from is None:
            raise ValueError("Invalid source unit: " + str(from_unit))

        liters = self._to_liters(target_value, normalized_to)
        return self._from_liters(liters, normalized_from)

if __name__ == '__main__':
    converter = VolumeConverter()

    result1 = converter.convert(1.0, 'gallon', 'liter')
    print(result1)

    result2 = converter.convert(1000.0, 'ml', 'fluid_ounce')
    print(result2)

    result3 = converter.convert(0.5, 'quart', 'cup')
    print(result3)

    result4 = converter.convert(2.0, 'pint', 'gallon')
    print(result4)

    batch_results = converter.batch_convert(
        [(1, 'liter'), (500, 'ml'), (1, 'gallon')],
        'ml'
    )
    print(batch_results)

    reverse_result = converter.reverse_convert(
        5.0,
        'liter',
        'gallon'
    )
    print(reverse_result)

    supported = converter.get_supported_units()
    print(len(supported))