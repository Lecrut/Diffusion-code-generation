class DistanceNormalizer:
    def __init__(self):
        self.conversion_factors = {
            'meter': 1.0,
            'm': 1.0,
            'kilometer': 1000.0,
            'km': 1000.0,
            'centimeter': 0.01,
            'cm': 0.01,
            'millimeter': 0.001,
            'mm': 0.001,
            'inch': 0.0254,
            'in': 0.0254,
            'foot': 0.3048,
            'ft': 0.3048,
            'yard': 0.9144,
            'yd': 0.9144,
            'mile': 1609.344,
            'mi': 1609.344,
            'nautical_mile': 1852.0,
            'nm': 1852.0,
        }

    def normalize(self, value, unit):
        unit_key = unit.lower().replace(' ', '_').replace('-', '_')
        if unit_key not in self.conversion_factors:
            raise ValueError(f"Unknown unit: {unit}")
        factor = self.conversion_factors[unit_key]
        return value * factor

if __name__ == '__main__':
    normalizer = DistanceNormalizer()
    result1 = normalizer.normalize(5, 'km')
    print(result1)
    result2 = normalizer.normalize(100, 'in')
    print(result2)
    result3 = normalizer.normalize(3.5, 'mile')
    print(result3)