class UnitConverter:

    def __init__(self, base_unit, conversion_factors):
        self.base_unit = base_unit
        self.conversion_factors = conversion_factors

    def convert(self, value, target_unit):
        if target_unit == self.base_unit:
            return value
        elif target_unit in self.conversion_factors:
            factor = self.conversion_factors[target_unit]
            return value * factor
        else:
            raise ValueError(f'Unsupported unit: {target_unit}')
if __name__ == '__main__':
    base_unit = 'meters'
    conversion_factors = {'centimeters': 100, 'kilometers': 0.001, 'inches': 39.3701, 'feet': 3.28084, 'yards': 1.09361}
    converter = UnitConverter(base_unit, conversion_factors)
    print(converter.convert(1, 'centimeters'))
    print(converter.convert(2, 'kilometers'))
    print(converter.convert(3, 'inches'))
    print(converter.convert(4, 'feet'))
    print(converter.convert(5, 'yards'))