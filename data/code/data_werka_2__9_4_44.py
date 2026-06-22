class VolumeConverter:

    def __init__(self):
        self.conversion_factors = {'L_to_ml': 1000, 'ml_to_L': 0.001, 'm3_to_gal': 264.172, 'gal_to_m3': 0.00378541}

    def convert(self, value, from_unit, to_unit):
        key = f'{from_unit}_to_{to_unit}'
        if key in self.conversion_factors:
            conversion_factor = self.conversion_factors[key]
            return value * conversion_factor
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported')
if __name__ == '__main__':
    converter = VolumeConverter()
    liters_to_milliliters = converter.convert(2, 'L', 'ml')
    cubic_meters_to_gallons = converter.convert(3, 'm3', 'gal')
    milliliters_to_liters = converter.convert(500, 'ml', 'L')
    gallons_to_cubic_meters = converter.convert(10, 'gal', 'm3')
    print(f'2 L is {liters_to_milliliters} ml')
    print(f'3 m³ is {cubic_meters_to_gallons} gal')
    print(f'500 ml is {milliliters_to_liters} L')
    print(f'10 gal is {gallons_to_cubic_meters} m³')