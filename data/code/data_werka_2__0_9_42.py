class LengthUnitConverter:
    def __init__(self):
        self._conversion_factors = {
            'meters_to_feet': 3.28084,
        }

    def convert(self, value, unit_pair):
        if unit_pair not in self._conversion_factors:
            raise ValueError(f"Unsupported conversion pair: {unit_pair}")
        if not isinstance(value, (int, float)):
            raise ValueError("Input value must be a numeric type.")
        return value * self._conversion_factors[unit_pair]

if __name__ == '__main__':
    converter = LengthUnitConverter()
    sample_value = 10
    unit_pair = 'meters_to_feet'
    try:
        result = converter.convert(sample_value, unit_pair)
        print(result)
    except ValueError as e:
        print(e)