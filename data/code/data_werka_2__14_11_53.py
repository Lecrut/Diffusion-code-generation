class VolumeEqualityChecker:

    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2

    def is_equal(self):
        return self.volume1 == self.volume2
if __name__ == '__main__':
    sample_volume_1 = 500.25
    sample_volume_2 = 500.25
    checker = VolumeEqualityChecker(sample_volume_1, sample_volume_2)
    equality_result = checker.is_equal()
    print(equality_result)