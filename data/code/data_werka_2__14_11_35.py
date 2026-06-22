class VolumeComparator:
    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2

    def compare(self):
        return self.volume1 == self.volume2

if __name__ == '__main__':
    sample_volumes = {
        'volume_a': 200.5,
        'volume_b': 200.5
    }
    
    comparator = VolumeComparator(sample_volumes['volume_a'], sample_volumes['volume_b'])
    result = comparator.compare()
    print(result)