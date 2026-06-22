class VolumeConverter:

    def __init__(self):
        self.conversion_factors = {'liters_to_milliliters': 1000, 'milliliters_to_liters': 1 / 1000, 'gallons_to_liters': 3.78541, 'liters_to_gallons': 1 / 3.78541, 'quarts_to_liters': 0.946353, 'liters_to_quarts': 1 / 0.946353, 'pints_to_liters': 0.473176, 'liters_to_pints': 1 / 0.473176, 'cups_to_liters': 0.236588, 'liters_to_cups': 1 / 0.236588, 'fluid_ounces_to_liters': 0.0295735, 'liters_to_fluid_ounces': 1 / 0.0295735}

    def convert(self, value, from_unit, to_unit):
        if f'{from_unit}_to_{to_unit}' in self.conversion_factors:
            return value * self.conversion_factors[f'{from_unit}_to_{to_unit}']
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported')
if __name__ == '__main__':
    converter = VolumeConverter()
    gallons_to_liters = converter.convert(5, 'gallons', 'liters')
    print(f'5 gallons is equal to {gallons_to_liters} liters')
    milliliters_to_cups = converter.convert(200, 'milliliters', 'cups')
    print(f'200 milliliters is equal to {milliliters_to_cups} cups')
    quarts_to_fluid_ounces = converter.convert(1, 'quarts', 'fluid_ounces')
    print(f'1 quart is equal to {quarts_to_fluid_ounces} fluid ounces')