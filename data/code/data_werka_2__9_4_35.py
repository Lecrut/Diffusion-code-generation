class VolumeUnit:

    def __init__(self, name, conversion_factor):
        self.name = name
        self.conversion_factor = conversion_factor

class VolumeConverter:

    def __init__(self):
        self.units = {'L': VolumeUnit('Liter', 1), 'ml': VolumeUnit('Milliliter', 0.001), 'm3': VolumeUnit('Cubic Meter', 1), 'gal': VolumeUnit('Gallon', 0.264172)}
        self.conversion_table = {('L', 'ml'): 1000, ('m3', 'gal'): 264.172}

    def convert(self, value, from_unit, to_unit):
        if (from_unit, to_unit) in self.conversion_table:
            return value * self.conversion_table[from_unit, to_unit]
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported')
if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, 'L', 'ml'))
    print(converter.convert(1, 'm3', 'gal'))