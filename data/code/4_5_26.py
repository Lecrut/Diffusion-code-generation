class DistanceConverter:

    def __init__(self):
        self.conversion_factors = {'m': 1, 'km': 1000, 'cm': 0.01, 'mm': 0.001, 'mi': 1609.34, 'ft': 0.3048, 'in': 0.0254}

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors:
            raise ValueError(f'Unsupported unit: {from_unit}')
        if to_unit not in self.conversion_factors:
            raise ValueError(f'Unsupported unit: {to_unit}')
        meters = value * self.conversion_factors[from_unit]
        converted_value = meters / self.conversion_factors[to_unit]
        return converted_value
if __name__ == '__main__':
    converter = DistanceConverter()
    sample_values = [(10, 'm', 'km'), (5, 'km', 'mi'), (100, 'cm', 'in'), (2, 'ft', 'mm')]
    for value, from_unit, to_unit in sample_values:
        try:
            result = converter.convert(value, from_unit, to_unit)
            print(f'{value} {from_unit} is {result:.4f} {to_unit}')
        except ValueError as e:
            print(e)