class ThresholdChecker:
    DEFAULT_THRESHOLD = 10

    @staticmethod
    def validate_input(value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be an integer or a float.")

    def __init__(self, threshold=DEFAULT_THRESHOLD):
        self.threshold = threshold
        self.generator = self._generator()

    def _generator(self):
        while True:
            value = yield
            ThresholdChecker.validate_input(value)
            if value > self.threshold:
                yield True
            else:
                yield False

    def send_value(self, value):
        return self.generator.send(value)

if __name__ == '__main__':
    checker = ThresholdChecker(10)
    next(checker.generator)
    values = [5, 15, 20, 8, 12]
    results = [checker.send_value(value) for value in values]
    print(results)