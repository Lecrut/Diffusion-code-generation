class VolumeConverter:

    def __init__(self, conversion_factors):
        self.conversion_factors = conversion_factors

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError('Invalid unit provided')
        factor_from = self.conversion_factors[from_unit]
        factor_to = self.conversion_factors[to_unit]
        return value * factor_from / factor_to
if __name__ == '__main__':
    conversion_factors = {'L': 1.0, 'ml': 0.001, 'm³': 1000.0, 'gal': 3.78541}
    converter = VolumeConverter(conversion_factors)
    print(converter.convert(2, 'L', 'ml'))
    print(converter.convert(1, 'm³', 'gal'))