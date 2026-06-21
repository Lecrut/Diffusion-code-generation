class DistanceConverter:
    def __init__(self):
        self.conversion_factors = {
            'meters': 1.0,
            'kilometers': 1000.0,
            'miles': 1609.344,
            'feet': 0.3048
        }

    def convert(self, value, source_unit):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a numeric type.")
        if source_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {source_unit}")
        
        meters = value * self.conversion_factors[source_unit]
        converted_values = {
            'meters': round(meters, 6),
            'kilometers': round(meters / 1000.0, 6),
            'miles': round(meters / 1609.344, 6),
            'feet': round(meters / 0.3048, 6)
        }
        
        return converted_values

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(100, 'meters'))
    print(converter.convert(100, 'kilometers'))
    print(converter.convert(100, 'miles'))
    print(converter.convert(100, 'feet'))