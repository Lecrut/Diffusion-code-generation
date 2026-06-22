class ThresholdChecker:
    def __init__(self, threshold=10):
        self.threshold = threshold

    def check(self, val_one, val_two):
        if not isinstance(val_one, int) or not isinstance(val_two, int):
            raise ValueError("Inputs must be integers")
        return val_one > self.threshold or val_two > self.threshold

if __name__ == '__main__':
    checker = ThresholdChecker()
    result = checker.check(12, 5)
    print(result)