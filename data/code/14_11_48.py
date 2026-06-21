class VolumeComparer:

    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2

    def is_equal(self):
        return self.volume1 == self.volume2

    def is_not_equal(self):
        return self.volume1 != self.volume2
if __name__ == '__main__':
    VOLUME_THRESHOLD = 0.0001
    volume_a = 500.0 + VOLUME_THRESHOLD
    volume_b = 500.0
    comparer = VolumeComparer(volume_a, volume_b)
    print('Are volumes equal?', comparer.is_equal())
    print('Are volumes not equal?', comparer.is_not_equal())