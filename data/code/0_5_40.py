class LengthConverter:
    def __init__(self):
        self.conversion_factors = {
            'm': 1,
            'cm': 0.01,
            'mm': 0.001,
            'km': 1000,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.34
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError('Unsupported unit')
        value_in_meters = value * self.conversion_factors[from_unit]
        converted_value = value_in_meters / self.conversion_factors[to_unit]
        return converted_value

if __name__ == '__main__':
    converter = LengthConverter()
    
    sample_value1 = 150
    from_unit1 = 'cm'
    to_unit1 = 'm'
    result1 = converter.convert(sample_value1, from_unit1, to_unit1)
    print(f"{sample_value1} {from_unit1} is {result1} {to_unit1}")

    sample_value2 = 5
    from_unit2 = 'mi'
    to_unit2 = 'km'
    result2 = converter.convert(sample_value2, from_unit2, to_unit2)
    print(f"{sample_value2} {from_unit2} is {result2} {to_unit2}")