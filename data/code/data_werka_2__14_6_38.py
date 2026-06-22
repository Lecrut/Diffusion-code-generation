class VolumeComparator:
    @staticmethod
    def compare_volumes(volume1, volume2):
        larger = max(volume1, volume2)
        smaller = min(volume1, volume2)
        difference = abs(volume1 - volume2)
        return larger, smaller, difference

if __name__ == '__main__':
    sample_volume1 = 5.678
    sample_volume2 = 2.345
    result = VolumeComparator.compare_volumes(sample_volume1, sample_volume2)
    print(result)