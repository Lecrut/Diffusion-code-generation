class LogicChecker:
    def evaluate(self, bool_list):
        if not bool_list:
            return True
        iterator = iter(bool_list)
        try:
            while True:
                if not next(iterator):
                    return False
        except StopIteration:
            return True

if __name__ == '__main__':
    checker = LogicChecker()
    test_cases = [
        [True, True, True],
        [True, False, True],
        [False, False],
        [True],
        [True, True, False, True]
    ]
    for i, case in enumerate(test_cases):
        result = checker.evaluate(case)
        print(f"Case {i + 1}: {result}")