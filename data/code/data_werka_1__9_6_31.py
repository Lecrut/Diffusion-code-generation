class VolumeConverter:

    def __init__(self):
        self.conversion_factors = {'L_to_ml': 1000, 'm3_to_gal': 264.172}

    def convert(self, value, from_unit, to_unit):
        key = f'{from_unit}_to_{to_unit}'
        if key in self.conversion_factors:
            return value * self.conversion_factors[key]
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported.')
if __name__ == '__main__':
    converter = VolumeConverter()
    liters_to_milliliters = converter.convert(1, 'L', 'ml')
    cubic_meters_to_gallons = converter.convert(1, 'm3', 'gal')
    print(f'1 L is {liters_to_milliliters} ml')
    print(f'1 m³ is {cubic_meters_to_gallons} gal')