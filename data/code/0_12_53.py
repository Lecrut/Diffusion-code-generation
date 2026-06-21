class LengthConverter:
    def __init__(self):
        self.conversion_factors = {
            'meters_to_kilometers': 1e-3,
            'meters_to_centimeters': 1e2,
            'meters_to_millimeters': 1e3,
            'meters_to_inches': 39.3701,
            'meters_to_feet': 3.28084,
            'meters_to_yards': 1.09361,
            'meters_to_miles': 6.21371e-4,
            'kilometers_to_meters': 1e3,
            'centimeters_to_meters': 1e-2,
            'millimeters_to_meters': 1e-3,
            'inches_to_meters': 0.0254,
            'feet_to_meters': 0.3048,
            'yards_to_meters': 0.9144,
            'miles_to_meters': 1609.34
        }

    def convert(self, value, from_unit, to_unit):
        key = f"{from_unit}_to_{to_unit}"
        if key in self.conversion_factors:
            return value * self.conversion_factors[key]
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")

if __name__ == '__main__':
    converter = LengthConverter()
    sample_values = [
        (10, 'meters', 'kilometers'),
        (500, 'centimeters', 'meters'),
        (2000, 'millimeters', 'meters'),
        (72, 'inches', 'meters'),
        (6, 'feet', 'meters'),
        (3, 'yards', 'meters'),
        (1, 'miles', 'meters')
    ]

    for value, from_unit, to_unit in sample_values:
        result = converter.convert(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {result:.6f} {to_unit}")