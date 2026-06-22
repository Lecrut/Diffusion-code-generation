class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            ('gram', 'ounce'): 0.035274
        }

    def convert(self, value, from_unit, to_unit):
        key = (from_unit, to_unit)
        if key in self.conversion_factors:
            result = value * self.conversion_factors[key]
            return round(result, 4)
        else:
            return "Conversion not supported for this pair."

if __name__ == '__main__':
    converter = UnitConverter()
    initial_value = 10
    from_unit = 'gram'
    to_unit = 'ounce'
    result = converter.convert(initial_value, from_unit, to_unit)
    print(result)