class VolumeComparison:
    def __init__(self, volume1, volume2):
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise ValueError("Volumes must be numeric values.")
        self.volume1 = volume1
        self.volume2 = volume2

    def are_equal(self):
        return self.volume1 == self.volume2

    def are_not_equal(self):
        return self.volume1 != self.volume2

if __name__ == '__main__':
    try:
        sample_volumes = {
            'volume_a': 300.75,
            'volume_b': 300.75
        }
        comparison = VolumeComparison(sample_volumes['volume_a'], sample_volumes['volume_b'])
        print(comparison.are_equal())
    except ValueError as e:
        print(e)