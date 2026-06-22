class LogicChecker:
    def evaluate(self, bool_values):
        if not bool_values:
            return True
        iterator = iter(bool_values)
        first = next(iterator)
        if not first:
            return False
        for val in iterator:
            if not val:
                return False
        return True

if __name__ == '__main__':
    checker = LogicChecker()
    test_cases = [
        [True, True, True],
        [True, False, True],
        [False, False, False],
        [True],
        []
    ]
    for i, case in enumerate(test_cases):
        result = checker.evaluate(case)
        print(f"Test {i + 1}: {result}")