class ConditionChecker:
    _MIN_THRESHOLD = 10
    _MAX_THRESHOLD = 200
    _DIVISOR_A = 3
    _DIVISOR_B = 5

    @staticmethod
    def _validate_range(value):
        return ConditionChecker._MIN_THRESHOLD <= value <= ConditionChecker._MAX_THRESHOLD

    @staticmethod
    def _check_divisibility_by_a(value):
        return value % ConditionChecker._DIVISOR_A == 0

    @staticmethod
    def _check_divisibility_by_b(value):
        return value % ConditionChecker._DIVISOR_B == 0

    @staticmethod
    def _check_not_square(value):
        root = int(value ** 0.5)
        return root * root != value

    @staticmethod
    def _check_positive(value):
        return value > 0

    def check_all(self, value):
        checks = [
            self._validate_range(value),
            self._check_divisibility_by_a(value),
            self._check_divisibility_by_b(value),
            self._check_not_square(value),
            self._check_positive(value),
        ]
        return all(checks)

if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.check_all(15)
    print(result)
    result = checker.check_all(300)
    print(result)
    result = checker.check_all(10)
    print(result)
    result = checker.check_all(9)
    print(result)
    result = checker.check_all(100)
    print(result)