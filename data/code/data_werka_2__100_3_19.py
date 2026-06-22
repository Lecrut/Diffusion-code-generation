class LogicChecker:
    def evaluate(self, bool_list):
        if not bool_list:
            return True
        for item in bool_list:
            if item is False:
                return False
        return True

if __name__ == '__main__':
    checker = LogicChecker()
    test_cases = [
        [True, True, True],
        [True, False, True],
        [False, False],
        [],
        [True],
        [True, True, False, True]
    ]
    for i, case in enumerate(test_cases):
        print(checker.evaluate(case))