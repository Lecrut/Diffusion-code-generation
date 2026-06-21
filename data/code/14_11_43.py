class VolumeAnalyzer:
    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2
        self._validate_volumes()

    def _validate_volumes(self):
        if not isinstance(self.volume1, (int, float)) or not isinstance(self.volume2, (int, float)):
            raise ValueError("Volumes must be numeric values.")

    def is_equal(self):
        return self.volume1 == self.volume2

    def is_not_equal(self):
        return self.volume1 != self.volume2

if __name__ == '__main__':
    sample_volumes = {
        'volume_a': 500.25,
        'volume_b': 500.25
    }
    analyzer = VolumeAnalyzer(sample_volumes['volume_a'], sample_volumes['volume_b'])
    print("Are volumes equal?", analyzer.is_equal())