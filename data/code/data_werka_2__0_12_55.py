class LengthConverter:

    def __init__(self):
        self.conversion_factors = {'meters_to_kilometers': 0.001, 'meters_to_centimeters': 100, 'meters_to_millimeters': 1000, 'meters_to_inches': 39.3701, 'meters_to_feet': 3.28084, 'meters_to_yards': 1.09361, 'meters_to_miles': 0.000621371, 'kilometers_to_meters': 1000, 'centimeters_to_meters': 0.01, 'millimeters_to_meters': 0.001, 'inches_to_meters': 0.0254, 'feet_to_meters': 0.3048, 'yards_to_meters': 0.9144, 'miles_to_meters': 1609.34}

    def convert(self, value, from_unit, to_unit):
        key = f'{from_unit}_to_{to_unit}'
        if key in self.conversion_factors:
            return value * self.conversion_factors[key]
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported.')
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(10, 'meters', 'kilometers'))
    print(converter.convert(100, 'centimeters', 'meters'))
    print(converter.convert(500, 'millimeters', 'inches'))
    print(converter.convert(10, 'feet', 'yards'))
    print(converter.convert(1, 'miles', 'kilometers'))