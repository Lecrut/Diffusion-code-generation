class VolumeComparator:

    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2

    def are_equal(self):
        return self.volume1 == self.volume2

    def are_not_equal(self):
        return self.volume1 != self.volume2
if __name__ == '__main__':
    comparator = VolumeComparator(100.0, 100.0)
    print(comparator.are_equal())
    print(comparator.are_not_equal())