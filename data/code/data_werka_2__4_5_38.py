class DistanceConverter:

    def __init__(self):
        self.conversion_factors = {'m': 1.0, 'km': 1000.0, 'cm': 0.01, 'mm': 0.001, 'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mi': 1609.34}

    def validate_unit(self, unit):
        if unit not in self.conversion_factors:
            raise ValueError(f'Unsupported unit: {unit}')

    def convert(self, distance, from_unit, to_unit):
        self.validate_unit(from_unit)
        self.validate_unit(to_unit)
        factor_from = self.conversion_factors[from_unit]
        factor_to = self.conversion_factors[to_unit]
        converted_distance = distance * factor_from / factor_to
        return converted_distance
if __name__ == '__main__':
    converter = DistanceConverter()
    distance_km = 10
    from_unit = 'km'
    to_unit = 'm'
    result_meters = converter.convert(distance_km, from_unit, to_unit)
    print(result_meters)
    distance_cm = 500
    from_unit = 'cm'
    to_unit = 'ft'
    result_feet = converter.convert(distance_cm, from_unit, to_unit)
    print(result_feet)