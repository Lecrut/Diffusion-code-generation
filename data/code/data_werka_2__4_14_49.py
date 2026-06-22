class DistanceNormalizer:
    def __init__(self):
        self.conversion_factors = {
            'meters': 1,
            'kilometers': 1000,
            'miles': 1609.34
        }

    def normalize(self, value, unit):
        if unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self.conversion_factors[unit]

if __name__ == '__main__':
    distances = [
        (10, 'meters'),
        (5, 'kilometers'),
        (2, 'miles')
    ]
    normalizer = DistanceNormalizer()
    for distance, unit in distances:
        normalized_distance = normalizer.normalize(distance, unit)
        print(f"{distance} {unit} is {normalized_distance} meters")