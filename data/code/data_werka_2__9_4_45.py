class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            'L_to_ml': 1000,
            'ml_to_L': 0.001,
            'm3_to_gal': 264.172,
            'gal_to_m3': 0.00378541
        }

    def convert(self, value, from_unit, to_unit):
        forward_key = f'{from_unit}_to_{to_unit}'
        reverse_key = f'{to_unit}_to_{from_unit}'

        if forward_key in self.conversion_factors:
            return value * self.conversion_factors[forward_key]
        elif reverse_key in self.conversion_factors:
            return value / self.conversion_factors[reverse_key]
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported')

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, 'L', 'ml'))
    print(converter.convert(1000, 'ml', 'L'))
    print(converter.convert(1, 'm3', 'gal'))
    print(converter.convert(1, 'gal', 'm3'))