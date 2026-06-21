class VolumeEvaluator:
    TOLERANCE = 1e-9

    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2

    def are_equal(self):
        return abs(self.volume1 - self.volume2) < self.TOLERANCE

    def are_not_equal(self):
        return not self.are_equal()

if __name__ == '__main__':
    VOLUME_A = 500.0
    VOLUME_B = 500.0
    evaluator = VolumeEvaluator(VOLUME_A, VOLUME_B)
    print("Are volumes equal?", evaluator.are_equal())
    print("Are volumes not equal?", evaluator.are_not_equal())