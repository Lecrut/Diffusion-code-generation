class VolumeAnalyzer:
    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2

    def is_equal(self):
        return self.volume1 == self.volume2

    def is_not_equal(self):
        return self.volume1 != self.volume2

if __name__ == '__main__':
    VOLUME_A = 500.0
    VOLUME_B = 500.0
    
    analyzer = VolumeAnalyzer(VOLUME_A, VOLUME_B)
    
    equality_result = analyzer.is_equal()
    inequality_result = analyzer.is_not_equal()
    
    print("Volumes are equal:", equality_result)
    print("Volumes are not equal:", inequality_result)