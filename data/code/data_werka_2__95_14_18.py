class ConditionChecker:
    FIRST_LOWER_BOUND = 0.0
    THIRD_RELATION = 'sum'

    @staticmethod
    def validate(first: float, second: float, third: float) -> bool:
        if not ConditionChecker._check_positive(first):
            return False
        if not ConditionChecker._check_order(first, second):
            return False
        if not ConditionChecker._check_sum(third, first, second):
            return False
        return True

    @staticmethod
    def _check_positive(value: float) -> bool:
        return value > ConditionChecker.FIRST_LOWER_BOUND

    @staticmethod
    def _check_order(first: float, second: float) -> bool:
        return second < first

    @staticmethod
    def _check_sum(expected: float, a: float, b: float) -> bool:
        return expected == a + b

if __name__ == '__main__':
    checker = ConditionChecker()
    val_a = 12.5
    val_b = 3.2
    val_c = 15.7
    outcome = checker.validate(val_a, val_b, val_c)
    print(outcome)