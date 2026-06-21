class ThresholdChecker:
    DEFAULT_THRESHOLD = 10

    @staticmethod
    def validate_value(value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be an integer or a float.")

    def __init__(self, threshold=DEFAULT_THRESHOLD):
        self.threshold = threshold

    def check_values(self, values):
        for value in values:
            ThresholdChecker.validate_value(value)
            yield value > self.threshold

if __name__ == '__main__':
    checker = ThresholdChecker(10)
    values = [5, 15, 20, 8, 12]
    results = list(checker.check_values(values))
    print(results)