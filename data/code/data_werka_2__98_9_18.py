class ConditionChecker:
    _MIN_VAL = 0
    _MAX_VAL = 100
    _REQUIRED_DIVISORS = (2, 3)

    def check_all(self, value):
        if value <= self._MIN_VAL:
            return False
        if value >= self._MAX_VAL:
            return False
        for divisor in self._REQUIRED_DIVISORS:
            if value % divisor != 0:
                return False
        return True

if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_all(6))
    print(checker.check_all(12))
    print(checker.check_all(0))
    print(checker.check_all(100))