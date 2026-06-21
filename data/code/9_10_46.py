class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000
    GALLONS_TO_LITERS = 3.78541
    QUARTS_TO_LITERS = 0.946353
    PINTS_TO_LITERS = 0.473176
    CUPS_TO_LITERS = 0.236588
    FLUID_OUNCES_TO_LITERS = 0.0295735

    def __init__(self):
        self.conversion_factors = {'liters_to_milliliters': self.LITERS_TO_MILLILITERS, 'milliliters_to_liters': 1 / self.LITERS_TO_MILLILITERS, 'gallons_to_liters': self.GALLONS_TO_LITERS, 'liters_to_gallons': 1 / self.GALLONS_TO_LITERS, 'quarts_to_liters': self.QUARTS_TO_LITERS, 'liters_to_quarts': 1 / self.QUARTS_TO_LITERS, 'pints_to_liters': self.PINTS_TO_LITERS, 'liters_to_pints': 1 / self.PINTS_TO_LITERS, 'cups_to_liters': self.CUPS_TO_LITERS, 'liters_to_cups': 1 / self.CUPS_TO_LITERS, 'fluid_ounces_to_liters': self.FLUID_OUNCES_TO_LITERS, 'liters_to_fluid_ounces': 1 / self.FLUID_OUNCES_TO_LITERS}

    def convert(self, value, from_unit, to_unit):
        key = f'{from_unit}_to_{to_unit}'
        if key in self.conversion_factors:
            return value * self.conversion_factors[key]
        else:
            raise ValueError('Invalid conversion units')
if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, 'liters', 'milliliters'))
    print(converter.convert(2, 'gallons', 'liters'))
    print(converter.convert(3, 'quarts', 'liters'))
    print(converter.convert(4, 'pints', 'liters'))
    print(converter.convert(5, 'cups', 'liters'))
    print(converter.convert(6, 'fluid_ounces', 'liters'))