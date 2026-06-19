class VolumeConverter:

    def __init__(self, conversion_factors):
        self.conversion_factors = conversion_factors

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError('Invalid unit')
        factor_from = self.conversion_factors[from_unit]
        factor_to = self.conversion_factors[to_unit]
        return value * factor_from / factor_to
if __name__ == '__main__':
    conversion_factors = {'L': 1000, 'm³': 264.172, 'ml': 1, 'gal': 3.78541}
    converter = VolumeConverter(conversion_factors)
    value_in_liters = 2.0
    converted_to_gallons = converter.convert(value_in_liters, 'L', 'gal')
    print(f'{value_in_liters} L is {converted_to_gallons:.4f} gal')