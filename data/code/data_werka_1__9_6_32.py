class VolumeConverter:

    def __init__(self):
        self.conversion_factors = {'L': {'ml': 1000, 'gal': 0.264172}, 'm³': {'gal': 264.172, 'L': 1000}}

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors[from_unit]:
            raise ValueError('Invalid unit conversion')
        factor = self.conversion_factors[from_unit][to_unit]
        return value * factor
if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, 'L', 'ml'))
    print(converter.convert(2, 'm³', 'gal'))