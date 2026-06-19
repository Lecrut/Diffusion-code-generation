class VolumeConverter:

    def __init__(self):
        self.conversion_factors = {'liters_to_milliliters': 1000, 'milliliters_to_liters': 0.001, 'liters_to_cubic_meters': 0.001, 'cubic_meters_to_liters': 1000, 'gallons_to_liters': 3.78541, 'liters_to_gallons': 0.264172, 'cubic_inches_to_liters': 0.0163871, 'liters_to_cubic_inches': 61.0237}

    def convert(self, value, from_unit, to_unit):
        key = f'{from_unit}_to_{to_unit}'
        if key in self.conversion_factors:
            return value * self.conversion_factors[key]
        else:
            raise ValueError('Invalid conversion units')
if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.convert(1, 'liters', 'milliliters'))
    print(converter.convert(1000, 'milliliters', 'liters'))
    print(converter.convert(1, 'cubic_meters', 'liters'))
    print(converter.convert(1000, 'liters', 'gallons'))
    print(converter.convert(1, 'gallons', 'cubic_inches'))