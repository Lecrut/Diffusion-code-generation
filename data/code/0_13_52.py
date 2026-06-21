class LengthConverter:
    def __init__(self):
        self.conversion_factors = {
            'm': {'cm': 100, 'in': 39.3701},
            'cm': {'m': 0.01, 'in': 0.393701},
            'in': {'m': 0.0254, 'cm': 2.54}
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {from_unit}")
        if to_unit not in self.conversion_factors[from_unit]:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        return value * self.conversion_factors[from_unit][to_unit]

if __name__ == '__main__':
    converter = LengthConverter()
    sample_values = [
        (1, 'm', 'cm'),
        (2.54, 'cm', 'in'),
        (10, 'in', 'm')
    ]
    for value, from_unit, to_unit in sample_values:
        converted_value = converter.convert(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {converted_value} {to_unit}")