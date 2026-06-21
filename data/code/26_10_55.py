class ThresholdEvaluator:
    DEFAULT_THRESHOLD = 10

    @staticmethod
    def validate_input(value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be an integer or a float.")

    def __init__(self, threshold=DEFAULT_THRESHOLD):
        self.threshold = threshold

    def evaluate(self):
        while True:
            value = yield
            self.validate_input(value)
            yield value > self.threshold

if __name__ == '__main__':
    evaluator = ThresholdEvaluator(10)
    generator = evaluator.evaluate()
    next(generator)
    values = [5, 15, 20, 8, 12]
    results = []
    for value in values:
        results.append(generator.send(value))
    print(results)