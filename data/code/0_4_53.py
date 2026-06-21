class UnitConverter:

    def __init__(self, base_unit, conversion_factors):
        self.base_unit = base_unit
        self.conversion_factors = conversion_factors

    def convert(self, value, target_unit):
        if target_unit not in self.conversion_factors:
            raise ValueError(f'Conversion to {target_unit} is not supported.')
        factor = self.conversion_factors[target_unit]
        return value * factor
if __name__ == '__main__':
    conversion_factors = {'meters': 1.0, 'centimeters': 100.0, 'millimeters': 1000.0, 'kilometers': 0.001, 'inches': 39.3701, 'feet': 3.28084, 'yards': 1.09361, 'miles': 0.000621371}
    converter = UnitConverter('meters', conversion_factors)
    print(converter.convert(1, 'centimeters'))
    print(converter.convert(2.5, 'kilometers'))
    print(converter.convert(10, 'inches'))