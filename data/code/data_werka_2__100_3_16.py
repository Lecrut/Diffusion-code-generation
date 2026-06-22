class LogicChecker:
    _DEFAULT_RESULT = True
    _FAILURE_RESULT = False

    @staticmethod
    def _check_value(value):
        return not value

    def evaluate(self, bool_list):
        if not bool_list:
            return self._DEFAULT_RESULT
        for item in bool_list:
            if self._check_value(item):
                return self._FAILURE_RESULT
        return self._DEFAULT_RESULT

if __name__ == '__main__':
    checker = LogicChecker()
    test_cases = [
        [True, True, True],
        [True, False, True],
        [False, False, False],
        [True],
        []
    ]
    for case in test_cases:
        result = checker.evaluate(case)
        print(result)