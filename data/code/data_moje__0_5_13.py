class UnitConverter:
    def __init__(self, base_unit, conversion_factors):
        self.base_unit = base_unit
        self.conversion_factors = conversion_factors

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit not in self.conversion_factors and from_unit != self.base_unit:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.conversion_factors and to_unit != self.base_unit:
            raise ValueError(f"Unknown unit: {to_unit}")
        if from_unit == self.base_unit:
            factor_to = self.conversion_factors[to_unit]
        elif to_unit == self.base_unit:
            factor_from = self.conversion_factors[from_unit]
            return value / factor_from
        else:
            factor_from = self.conversion_factors[from_unit]
            factor_to = self.conversion_factors[to_unit]
            return (value / factor_from) * factor_to

if __name__ == '__main__':
    factors = {
        'km': 1000.0,
        'm': 1.0,
        'cm': 0.01,
        'mm': 0.001,
        'ft': 0.3048,
        'in': 0.0254,
        'mi': 1609.344
    }
    converter = UnitConverter('m', factors)
    print(converter.convert(1, 'mi', 'km'))
    print(converter.convert(100, 'cm', 'in'))
    print(converter.convert(5, 'ft', 'm'))