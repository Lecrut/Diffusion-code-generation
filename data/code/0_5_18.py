class UnitConverter:
    def __init__(self, base_unit, conversion_factors):
        self.base_unit = base_unit
        self.conversion_factors = conversion_factors
        self.conversion_factors[base_unit] = 1.0

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unit {from_unit} is not recognized")
        if to_unit not in self.conversion_factors:
            raise ValueError(f"Unit {to_unit} is not recognized")

        factor_from = self.conversion_factors[from_unit]
        factor_to = self.conversion_factors[to_unit]

        base_value = value * factor_from
        result = base_value / factor_to

        return result

if __name__ == '__main__':
    conversion_factors = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'centimeters': 0.01,
        'miles': 1609.34,
        'feet': 0.3048,
        'inches': 0.0254
    }

    converter = UnitConverter('meters', conversion_factors)

    result1 = converter.convert(5, 'kilometers', 'miles')
    print(result1)

    result2 = converter.convert(100, 'miles', 'kilometers')
    print(result2)

    result3 = converter.convert(1, 'miles', 'feet')
    print(result3)

    result4 = converter.convert(12, 'inches', 'meters')
    print(result4)

    result5 = converter.convert(500, 'centimeters', 'kilometers')
    print(result5)