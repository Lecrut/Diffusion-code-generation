class LengthConverter:
    def __init__(self):
        self.conversion_factors = {
            'm': 1.0,
            'ft': 0.3048,
            'cm': 0.01,
            'km': 1000.0,
            'mm': 0.001
        }

    def convert_to_meters(self, value, unit):
        if unit in self.conversion_factors:
            return value * self.conversion_factors[unit]
        else:
            raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    converter = LengthConverter()
    sample_feet = 10
    meters = converter.convert_to_meters(sample_feet, 'ft')
    print(meters)