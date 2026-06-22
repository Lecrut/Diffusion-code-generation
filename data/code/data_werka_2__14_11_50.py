class VolumeEvaluator:
    def __init__(self, volume1, volume2):
        self.volume1 = volume1
        self.volume2 = volume2

    def evaluate(self):
        return self.volume1 == self.volume2

if __name__ == '__main__':
    sample_volumes = {
        'volume_a': 500.0,
        'volume_b': 500.0
    }
    evaluator = VolumeEvaluator(sample_volumes['volume_a'], sample_volumes['volume_b'])
    result = evaluator.evaluate()
    print(result)