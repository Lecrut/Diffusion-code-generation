class VolumeConverter:

    def __init__(self, conversion_factors):
        self.conversion_factors = conversion_factors

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        intermediate_value = value * self.conversion_factors[from_unit]
        converted_value = intermediate_value / self.conversion_factors[to_unit]
        return converted_value
if __name__ == '__main__':
    conversion_factors = {'L': 1.0, 'ml': 0.001, 'm³': 1000.0, 'gal': 3.78541}
    converter = VolumeConverter(conversion_factors)
    result = converter.convert(2.0, 'L', 'gal')
    print(result)