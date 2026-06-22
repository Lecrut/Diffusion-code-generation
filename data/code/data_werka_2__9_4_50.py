class VolumeConverter:

    def __init__(self):
        self.conversion_factors = {'L_to_ml': 1000, 'm3_to_gal': 264.172, 'ml_to_L': 0.001, 'gal_to_m3': 0.00378541}

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
    milliliters_to_liters = converter.convert(1000, 'ml', 'L')
    gallons_to_cubic_meters = converter.convert(1, 'gal', 'm3')
    print(f'1 L to ml: {liters_to_milliliters}')
    print(f'1 m³ to gal: {cubic_meters_to_gallons}')
    print(f'1000 ml to L: {milliliters_to_liters}')
    print(f'1 gal to m³: {gallons_to_cubic_meters}')