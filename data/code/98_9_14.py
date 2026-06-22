class ConditionChecker:
    def __init__(self):
        self.thresholds = (10, 50, 100)
        self.multipliers = (2, 5)

    def _check_range(self, value):
        return self.thresholds[0] < value < self.thresholds[2]

    def _check_divisibility(self, value):
        return value % self.multipliers[0] == 0 or value % self.multipliers[1] == 0

    def _check_sign(self, value):
        return value > 0

    def check_all(self, value):
        if not self._check_sign(value):
            return False
        if not self._check_range(value):
            return False
        if not self._check_divisibility(value):
            return False
        return True

if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_all(10))
    print(checker.check_all(20))
    print(checker.check_all(105))
    print(checker.check_all(-5))