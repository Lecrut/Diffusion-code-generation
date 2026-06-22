class UnitConverter:
    def __init__(self, base_unit, conversion_factors):
        self.base_unit = base_unit
        self.conversion_factors = conversion_factors

    def to_base(self, amount, unit):
        if unit == self.base_unit:
            return amount
        if unit not in self.conversion_factors:
            raise ValueError(f"Unknown unit: {unit}")
        return amount * self.conversion_factors[unit]

    def from_base(self, amount, target_unit):
        if target_unit == self.base_unit:
            return amount
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Unknown unit: {target_unit}")
        return amount / self.conversion_factors[target_unit]

    def convert(self, amount, source_unit, target_unit):
        if source_unit == target_unit:
            return amount
        base_amount = self.to_base(amount, source_unit)
        return self.from_base(base_amount, target_unit)

def convert_unit(amount, source_unit, target_unit, base_unit, conversion_factors):
    converter = UnitConverter(base_unit, conversion_factors)
    return converter.convert(amount, source_unit, target_unit)

if __name__ == '__main__':
    base_unit = 'meters'
    conversion_factors = {
        'kilometers': 1000.0,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254
    }

    result1 = convert_unit(1, 'kilometers', 'meters', base_unit, conversion_factors)
    print(result1)

    result2 = convert_unit(100, 'feet', 'meters', base_unit, conversion_factors)
    print(result2)

    result3 = convert_unit(5, 'meters', 'inches', base_unit, conversion_factors)
    print(result3)

    result4 = convert_unit(1, 'miles', 'kilometers', base_unit, conversion_factors)
    print(result4)

    converter = UnitConverter(base_unit, conversion_factors)
    result5 = converter.convert(10, 'yards', 'centimeters', base_unit)
    print(result5)

    result6 = converter.convert(1, 'inches', 'meters', base_unit)
    print(result6)

    result7 = converter.convert(1000, 'meters', 'kilometers', base_unit)
    print(result7)

    result8 = converter.convert(0.5, 'miles', 'feet', base_unit)
    print(result8)

    result9 = converter.convert(3.5, 'centimeters', 'millimeters', base_unit)
    print(result9)

    result10 = converter.convert(100, 'meters', 'meters', base_unit)
    print(result10)