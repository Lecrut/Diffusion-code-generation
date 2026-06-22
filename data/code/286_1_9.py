class LengthConverter:

    def __init__(self):
        self.conversion_factors = {'m': 1.0, 'cm': 0.01, 'km': 1000.0, 'mm': 0.001}

    def convert_to_meters(self, value, unit):
        try:
            return float(value) * self.conversion_factors[unit]
        except (ValueError, KeyError):
            return None
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert_to_meters(10, 'cm'))
    print(converter.convert_to_meters(5, 'km'))
    print(converter.convert_to_meters(2, 'mm'))