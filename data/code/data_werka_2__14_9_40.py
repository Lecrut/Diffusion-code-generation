class VolumeComparator:

    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2

    def compare(self):
        if not isinstance(self.volume1, (int, float)) or not isinstance(self.volume2, (int, float)):
            raise ValueError('Both volumes must be numbers')
        if self.volume1 > self.volume2:
            return 'Volume 1 is larger'
        elif self.volume1 < self.volume2:
            return 'Volume 2 is larger'
        else:
            return 'Volumes are equal'
if __name__ == '__main__':
    comparator = VolumeComparator(50.0, 75.0)
    print(comparator.compare())
    comparator = VolumeComparator(100.0, 100.0)
    print(comparator.compare())
    comparator = VolumeComparator(200.3, 150.5)
    print(comparator.compare())