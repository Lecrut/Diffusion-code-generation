class VolumeAnalyzer:
    VOLUME_TOLERANCE = 1e-9

    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2

    @staticmethod
    def are_volumes_equal(volume1, volume2, tolerance=VOLUME_TOLERANCE):
        return abs(volume1 - volume2) < tolerance

    def compare(self):
        return VolumeAnalyzer.are_volumes_equal(self.volume1, self.volume2)

if __name__ == '__main__':
    volume_a = 500.0
    volume_b = 500.0
    analyzer = VolumeAnalyzer(volume_a, volume_b)
    result = analyzer.compare()
    print(result)