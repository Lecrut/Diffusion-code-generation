class VolumeComparer:
    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2

    def is_equal(self):
        return self.volume1 == self.volume2

    def is_not_equal(self):
        return self.volume1 != self.volume2

if __name__ == '__main__':
    sample_volumes = {
        'volume_a': 500.0,
        'volume_b': 500.0
    }
    comparer = VolumeComparer(sample_volumes['volume_a'], sample_volumes['volume_b'])
    print(comparer.is_equal())