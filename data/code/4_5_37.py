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

    def convert(self, distance, from_unit, to_unit):
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported target unit: {to_unit}")

        factor_from = self.conversion_factors[from_unit]
        factor_to = self.conversion_factors[to_unit]

        converted_distance = distance * (factor_to / factor_from)
        return converted_distance

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_distance = 10
    from_unit = 'km'
    to_unit = 'm'

    try:
        result = converter.convert(sample_distance, from_unit, to_unit)
        print(f"{sample_distance} {from_unit} is equal to {result} {to_unit}")
    except ValueError as e:
        print(e)