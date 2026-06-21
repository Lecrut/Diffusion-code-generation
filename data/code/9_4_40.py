class VolumeConverter:

    def __init__(self):
        self.conversion_factors = {'L': {'ml': 1000}, 'm3': {'gal': 264.172}}

    def convert(self, value, from_unit, to_unit):
        if from_unit in self.conversion_factors and to_unit in self.conversion_factors[from_unit]:
            return value * self.conversion_factors[from_unit][to_unit]
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported')
if __name__ == '__main__':
    converter = VolumeConverter()
    result1 = converter.convert(2, 'L', 'ml')
    print(result1)
    result2 = converter.convert(0.5, 'm3', 'gal')
    print(result2)