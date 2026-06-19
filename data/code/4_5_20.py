class DistanceConverter:
    def __init__(self):
        self.conversion_factors = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.34
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {from_unit}")
        if to_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {to_unit}")

        factor_from = self.conversion_factors[from_unit]
        factor_to = self.conversion_factors[to_unit]

        converted_value = value * (factor_from / factor_to)
        return converted_value

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_values = [
        (10, 'm', 'km'),
        (5, 'in', 'cm'),
        (2, 'yd', 'm')
    ]

    for value, from_unit, to_unit in sample_values:
        try:
            result = converter.convert(value, from_unit, to_unit)
            print(f"{value} {from_unit} is {result:.4f} {to_unit}")
        except ValueError as e:
            print(e)