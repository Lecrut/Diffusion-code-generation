class VolumeConverter:

    def __init__(self):
        self.conversion_factors = {'L_to_ml': 1000, 'm3_to_gal': 264.172, 'ml_to_L': 0.001, 'gal_to_m3': 0.00378541}

    def convert(self, value, from_unit, to_unit):
        conversion_key = f'{from_unit}_to_{to_unit}'
        if conversion_key in self.conversion_factors:
            return value * self.conversion_factors[conversion_key]
        else:
            raise ValueError('Unsupported conversion')
if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, 'L', 'ml'))
    print(converter.convert(2, 'm3', 'gal'))
    print(converter.convert(1000, 'ml', 'L'))
    print(converter.convert(10, 'gal', 'm3'))