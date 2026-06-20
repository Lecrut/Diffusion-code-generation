class DistanceNormalizer:
    def __init__(self):
        self.factors = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.344,
            'nm': 1e-9,
            'um': 1e-6,
            'nmi': 1852.0
        }

    def normalize(self, value, unit):
        normalized_unit = unit.lower()
        if normalized_unit not in self.factors:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self.factors[normalized_unit]

if __name__ == '__main__':
    normalizer = DistanceNormalizer()
    sample_inputs = [
        (100, 'cm'),
        (1.5, 'mi'),
        (25, 'ft'),
        (3, 'km'),
        (500, 'in')
    ]
    for val, u in sample_inputs:
        result = normalizer.normalize(val, u)
        print(f"{val} {u} = {result} m")