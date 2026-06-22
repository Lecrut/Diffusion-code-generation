class VolumeEvaluator:
    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2
    
    def evaluate(self):
        return self.volume1 == self.volume2

if __name__ == '__main__':
    sample_volume_a = 500.25
    sample_volume_b = 500.25
    evaluator = VolumeEvaluator(sample_volume_a, sample_volume_b)
    equality_result = evaluator.evaluate()
    print(equality_result)