class LengthConverter:
    def __init__(self):
        self.conversion_factors = {
            ('m', 'ft'): 3.28084,
            ('ft', 'm'): 1 / 3.28084
        }

    def convert(self, value, from_unit, to_unit):
        conversion_key = (from_unit, to_unit)
        if conversion_key in self.conversion_factors:
            return value * self.conversion_factors[conversion_key]
        else:
            raise ValueError('Unsupported unit conversion')

if __name__ == '__main__':
    converter = LengthConverter()
    sample_value_meters = 15
    sample_value_feet = 50

    converted_to_feet = converter.convert(sample_value_meters, 'm', 'ft')
    converted_to_meters = converter.convert(sample_value_feet, 'ft', 'm')

    print(f"{sample_value_meters} meters is {converted_to_feet} feet")
    print(f"{sample_value_feet} feet is {converted_to_meters} meters")