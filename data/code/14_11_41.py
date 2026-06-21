class VolumeEqualityChecker:
    def __init__(self, volume1, volume2):
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise ValueError("Both volumes must be numeric values.")
        self.volume1 = volume1
        self.volume2 = volume2

    def is_equal(self):
        return self.volume1 == self.volume2

if __name__ == '__main__':
    try:
        sample_volumes = {
            'volume_a': 500.0,
            'volume_b': 500.0
        }
        checker = VolumeEqualityChecker(sample_volumes['volume_a'], sample_volumes['volume_b'])
        result = checker.is_equal()
        print(result)
    except ValueError as e:
        print(e)