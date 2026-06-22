class BooleanChecker:
    TRUE_VALUE = True
    FALSE_VALUE = False

    @staticmethod
    def is_any_true(values):
        if not values:
            return False
        return any(BooleanChecker._validate(v) for v in values)

    @staticmethod
    def _validate(value):
        if not isinstance(value, bool):
            raise ValueError("All elements must be boolean")
        return value

if __name__ == '__main__':
    test_cases = [
        [False, False, False],
        [False, True, False],
        [True, True, True],
        [False, False, True, False]
    ]
    for case in test_cases:
        checker = BooleanChecker()
        result = checker.is_any_true(case)
        print(result)