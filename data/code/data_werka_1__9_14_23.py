class VolumeConverter:

    def __init__(self):
        self.conversion_factors = {'liters_to_milliliters': 1000, 'milliliters_to_liters': 0.001, 'liters_to_gallons': 0.264172, 'gallons_to_liters': 3.78541, 'liters_to_quarts': 1.05669, 'quarts_to_liters': 0.946353, 'liters_to_pints': 2.11338, 'pints_to_liters': 0.473176, 'liters_to_cups': 4.22675, 'cups_to_liters': 0.236588, 'liters_to_fluid_ounces': 33.814, 'fluid_ounces_to_liters': 0.0295735}

    def convert(self, value, from_unit, to_unit):
        key = f'{from_unit.lower()}_to_{to_unit.lower()}'
        if key in self.conversion_factors:
            return value * self.conversion_factors[key]
        else:
            raise ValueError('Invalid conversion units')
if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, 'liters', 'milliliters'))
    print(converter.convert(2, 'gallons', 'liters'))
    print(converter.convert(3, 'quarts', 'pints'))
    print(converter.convert(4, 'cups', 'fluid_ounces'))