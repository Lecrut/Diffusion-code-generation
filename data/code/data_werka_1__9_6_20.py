class VolumeConverter:

    def __init__(self):
        self.conversion_factors = {'L_to_ml': 1000, 'm3_to_L': 1000, 'L_to_gal': 0.264172, 'gal_to_L': 3.78541, 'm3_to_gal': 264.172, 'gal_to_m3': 0.00378541}

    def convert(self, value, from_unit, to_unit):
        key = f'{from_unit}_to_{to_unit}'
        if key in self.conversion_factors:
            return value * self.conversion_factors[key]
        else:
            raise ValueError('Unsupported conversion')
if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, 'L', 'ml'))
    print(converter.convert(1, 'm3', 'gal'))
    print(converter.convert(1, 'L', 'gal'))