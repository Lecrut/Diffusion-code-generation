TOLERANCE = 1e-9

def are_volumes_equal(volume1, volume2):
    return abs(volume1 - volume2) < TOLERANCE

class VolumeEqualityChecker:
    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2
    
    def check(self):
        return are_volumes_equal(self.volume1, self.volume2)

if __name__ == '__main__':
    VOLUME_A = 500.0
    VOLUME_B = 500.0
    checker = VolumeEqualityChecker(VOLUME_A, VOLUME_B)
    result = checker.check()
    print(result)