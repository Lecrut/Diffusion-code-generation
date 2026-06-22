class VolumeConverter:
    def __init__(self):
        self.base_units = {'L': 1.0, 'ml': 0.001, 'm3': 1.0, 'gal': 3.78541}
        self.conversion_table = {
            ('L', 'ml'): lambda x: x * 1000,
            ('ml', 'L'): lambda x: x / 1000,
            ('m3', 'gal'): lambda x: x * 264.172,
            ('gal', 'm3'): lambda x: x / 264.172
        }

    def convert(self, value, from_unit, to_unit):
        if (from_unit, to_unit) in self.conversion_table:
            return self.conversion_table[(from_unit, to_unit)](value)
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported')

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, 'L', 'ml'))
    print(converter.convert(1, 'm3', 'gal'))
    print(converter.convert(1000, 'ml', 'L'))
    print(converter.convert(1, 'gal', 'm3'))