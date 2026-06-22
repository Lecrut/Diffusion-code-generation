class DistanceConverter:
    def __init__(self):
        self.conversion_factors = {
            'meters': 1.0,
            'kilometers': 1000.0,
            'miles': 1609.344,
            'feet': 0.3048
        }

    def convert_to_meters(self, value, source_unit):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a numeric type.")
        if source_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {source_unit}")
        return value * self.conversion_factors[source_unit]

    def convert(self, value, source_unit, target_unit):
        meters = self.convert_to_meters(value, source_unit)
        if target_unit == 'meters':
            return round(meters, 6)
        elif target_unit == 'kilometers':
            return round(meters / 1000.0, 6)
        elif target_unit == 'miles':
            return round(meters / 1609.344, 6)
        elif target_unit == 'feet':
            return round(meters / 0.3048, 6)
        else:
            raise ValueError(f"Unsupported target unit: {target_unit}")

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(100, 'meters', 'kilometers'))
    print(converter.convert(100, 'kilometers', 'miles'))
    print(converter.convert(100, 'miles', 'feet'))
    print(converter.convert(100, 'feet', 'meters'))