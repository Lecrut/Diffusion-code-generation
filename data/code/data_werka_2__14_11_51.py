class VolumeEqualityChecker:
    VOLUME_TOLERANCE = 1e-9

    @staticmethod
    def are_volumes_equal(volume1, volume2):
        return abs(volume1 - volume2) < VolumeEqualityChecker.VOLUME_TOLERANCE

if __name__ == '__main__':
    volume_a = 500.0
    volume_b = 500.0
    result = VolumeEqualityChecker.are_volumes_equal(volume_a, volume_b)
    print(result)