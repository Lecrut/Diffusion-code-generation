class DistanceConverter:
    def __init__(self):
        self.conversion_factors = {
            ('meters', 'kilometers'): 0.001,
            ('kilometers', 'meters'): 1000,
            ('meters', 'miles'): 0.000621371,
            ('miles', 'meters'): 1609.34,
            ('kilometers', 'miles'): 0.621371,
            ('miles', 'kilometers'): 1.60934,
        }
        self.supported_units = {'meters', 'kilometers', 'miles'}

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.supported_units:
            raise ValueError(f"Unsupported unit: {from_unit}")
        if to_unit not in self.supported_units:
            raise ValueError(f"Unsupported unit: {to_unit}")
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if from_unit == to_unit:
            return float(value)
        factor = self.conversion_factors[(from_unit, to_unit)]
        return float(value * factor)

if __name__ == '__main__':
    converter = DistanceConverter()
    result1 = converter.convert(1000, 'meters', 'kilometers')
    print(result1)
    result2 = converter.convert(1, 'kilometers', 'miles')
    print(result2)
    result3 = converter.convert(1, 'miles', 'meters')
    print(result3)
    result4 = converter.convert(500, 'meters', 'meters')
    print(result4)