class ThresholdEvaluator:
    THRESHOLD = 10

    @staticmethod
    def validate_input(value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be an integer or a float.")

    def __init__(self, threshold=THRESHOLD):
        self.threshold = threshold
        self.generator = self._generator()

    def _generator(self):
        while True:
            value = yield
            ThresholdEvaluator.validate_input(value)
            if value > self.threshold:
                yield True
            else:
                yield False

    def send(self, value):
        return self.generator.send(value)

if __name__ == '__main__':
    evaluator = ThresholdEvaluator(10)
    next(evaluator.generator)
    values = [5, 15, 20, 8, 12]
    results = []
    for value in values:
        results.append(evaluator.send(value))
    print(results)