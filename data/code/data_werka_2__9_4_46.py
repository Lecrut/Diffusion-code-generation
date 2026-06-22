class VolumeConverter:

    def __init__(self):
        self.conversion_factors = {'L_to_ml': 1000, 'ml_to_L': 0.001, 'm3_to_gal': 264.172, 'gal_to_m3': 0.00378541}

    def convert(self, value, from_unit, to_unit):
        key = f'{from_unit}_to_{to_unit}'
        if key in self.conversion_factors:
            return value * self.conversion_factors[key]
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported')
if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, 'L', 'ml'))
    print(converter.convert(2, 'm3', 'gal'))