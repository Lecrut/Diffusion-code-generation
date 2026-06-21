class VolumeConverter:
    L_TO_ML = 1000
    M3_TO_GAL = 264.172

    def __init__(self):
        self.conversion_factors = {
            'L': {'ml': self.L_TO_ML},
            'm3': {'gal': self.M3_TO_GAL}
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit in self.conversion_factors and to_unit in self.conversion_factors[from_unit]:
            return value * self.conversion_factors[from_unit][to_unit]
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported')

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, 'L', 'ml'))
    print(converter.convert(1, 'm3', 'gal'))