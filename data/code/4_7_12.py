class DistanceNormalizer:
    def __init__(self):
        self.scale_factors = {
            'm': 1.0,
            'meter': 1.0,
            'meters': 1.0,
            'km': 1000.0,
            'kilometer': 1000.0,
            'kilometers': 1000.0,
            'cm': 0.01,
            'centimeter': 0.01,
            'centimeters': 0.01,
            'mm': 0.001,
            'millimeter': 0.001,
            'millimeters': 0.001,
            'in': 0.0254,
            'inch': 0.0254,
            'inches': 0.0254,
            'ft': 0.3048,
            'foot': 0.3048,
            'feet': 0.3048,
            'yd': 0.9144,
            'yard': 0.9144,
            'yards': 0.9144,
            'mi': 1609.344,
            'mile': 1609.344,
            'miles': 1609.344
        }

    def normalize_to_meters(self, value, unit):
        if unit not in self.scale_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self.scale_factors[unit]

if __name__ == '__main__':
    normalizer = DistanceNormalizer()
    sample_value_1 = 5.0
    sample_unit_1 = 'km'
    sample_value_2 = 12.0
    sample_unit_2 = 'ft'
    result_1 = normalizer.normalize_to_meters(sample_value_1, sample_unit_1)
    result_2 = normalizer.normalize_to_meters(sample_value_2, sample_unit_2)
    print(result_1)
    print(result_2)