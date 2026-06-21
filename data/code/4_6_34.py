class DistanceNormalizer:
    def __init__(self):
        self.conversion_factors = {
            'm': 1,
            'km': 1000,
            'cm': 0.01,
            'mm': 0.001,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.34
        }

    def normalize(self, distance, unit):
        if unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        return distance * self.conversion_factors[unit]

if __name__ == '__main__':
    normalizer = DistanceNormalizer()
    sample_values = [
        (10, 'km'),
        (500, 'm'),
        (12, 'in'),
        (3, 'yd'),
        (2.5, 'mi')
    ]
    for distance, unit in sample_values:
        normalized = normalizer.normalize(distance, unit)
        print(f'{distance} {unit} is {normalized} meters')