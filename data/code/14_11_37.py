class VolumeChecker:
    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2

    def check_equality(self):
        return self.volume1 == self.volume2

    def check_inequality(self):
        return self.volume1 != self.volume2

if __name__ == '__main__':
    volume_a = 400.0
    volume_b = 400.0
    checker = VolumeChecker(volume_a, volume_b)
    print("Are volumes equal?", checker.check_equality())
    print("Are volumes not equal?", checker.check_inequality())