class VolumeConverter:
    CONVERSIONS = {'liters_to_milliliters': 1000, 'milliliters_to_liters': 1 / 1000, 'gallons_to_liters': 3.78541, 'liters_to_gallons': 1 / 3.78541, 'quarts_to_liters': 0.946353, 'liters_to_quarts': 1 / 0.946353, 'pints_to_liters': 0.473176, 'liters_to_pints': 1 / 0.473176, 'cups_to_liters': 0.236588, 'liters_to_cups': 1 / 0.236588, 'fluid_ounces_to_liters': 0.0295735, 'liters_to_fluid_ounces': 1 / 0.0295735}

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.CONVERSIONS or to_unit not in self.CONVERSIONS:
            raise ValueError('Unsupported unit')
        conversion_key = f'{from_unit}_to_liters'
        intermediate_value = value * self.CONVERSIONS[conversion_key]
        conversion_key = f'liters_to_{to_unit}'
        result = intermediate_value * self.CONVERSIONS[conversion_key]
        return result
if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, 'liters', 'milliliters'))
    print(converter.convert(500, 'milliliters', 'liters'))
    print(converter.convert(1, 'gallons', 'liters'))
    print(converter.convert(2, 'liters', 'quarts'))
    print(converter.convert(16, 'fluid_ounces', 'liters'))