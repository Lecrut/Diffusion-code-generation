class VolumeAnalyzer:
    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2

    def is_equal(self):
        return self.volume1 == self.volume2

    def is_not_equal(self):
        return self.volume1 != self.volume2

if __name__ == '__main__':
    sample_volumes = {
        'volume_a': 500.2,
        'volume_b': 500.2
    }
    analyzer = VolumeAnalyzer(sample_volumes['volume_a'], sample_volumes['volume_b'])
    print("Volumes are equal:", analyzer.is_equal())
    print("Volumes are not equal:", analyzer.is_not_equal())