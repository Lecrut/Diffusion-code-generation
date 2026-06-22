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
    conversion_factors = {'L': 1000, 'm³': 264.172, 'ml': 1, 'gal': 3.78541}
    converter = VolumeConverter(conversion_factors)
    sample_value = 2
    from_unit = 'L'
    to_unit = 'ml'
    result = converter.convert(sample_value, from_unit, to_unit)
    print(f'{sample_value} {from_unit} is equal to {result} {to_unit}')