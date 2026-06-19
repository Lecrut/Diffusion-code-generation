class VolumeConverter:

    def __init__(self, conversion_factors):
        self.conversion_factors = conversion_factors

    def convert(self, value, from_unit, to_unit):
        factor_from = self.conversion_factors.get(from_unit)
        factor_to = self.conversion_factors.get(to_unit)
        if not factor_from or not factor_to:
            raise ValueError('Invalid unit provided')
        return value * factor_from / factor_to
conversion_factors = {'L': 1.0, 'ml': 1000.0, 'm³': 0.001, 'gal': 0.264172}
if __name__ == '__main__':
    converter = VolumeConverter(conversion_factors)
    print(converter.convert(1, 'L', 'ml'))
    print(converter.convert(1, 'm³', 'gal'))
    print(converter.convert(500, 'ml', 'L'))