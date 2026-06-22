class VolumeConverter:
    CONVERSIONS = {'liters_to_milliliters': 1000, 'milliliters_to_liters': 1 / 1000, 'gallons_to_liters': 3.78541, 'liters_to_gallons': 1 / 3.78541, 'quarts_to_liters': 0.946353, 'liters_to_quarts': 1 / 0.946353, 'pints_to_liters': 0.473176, 'liters_to_pints': 1 / 0.473176, 'cups_to_liters': 0.236588, 'liters_to_cups': 1 / 0.236588, 'fluid_ounces_to_liters': 0.0295735, 'liters_to_fluid_ounces': 1 / 0.0295735}

    def convert(self, from_unit, to_unit, value):
        key = f'{from_unit}_to_{to_unit}'
        if key in self.CONVERSIONS:
            return value * self.CONVERSIONS[key]
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported')
if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert('liters', 'milliliters', 2.5))
    print(converter.convert('gallons', 'liters', 1))
    print(converter.convert('quarts', 'pints', 4))
    print(converter.convert('cups', 'fluid_ounces', 2))