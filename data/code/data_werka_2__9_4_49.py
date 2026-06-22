class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            'L': {'ml': 1000, 'm3': 0.001},
            'ml': {'L': 0.001, 'm3': 0.000001},
            'm3': {'L': 1000, 'gal': 264.172},
            'gal': {'m3': 0.00378541}
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors:
            raise ValueError(f'Unit {from_unit} is not supported')
        if to_unit not in self.conversion_factors[from_unit]:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported')

        conversion_factor = self.conversion_factors[from_unit][to_unit]
        return value * conversion_factor

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, 'L', 'ml'))
    print(converter.convert(1, 'm3', 'gal'))
    print(converter.convert(1000, 'ml', 'L'))
    print(converter.convert(1, 'gal', 'm3'))