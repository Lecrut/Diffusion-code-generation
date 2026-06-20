class BooleanChecker:
    def __init__(self, bool_list):
        self.bool_list = bool_list

    def check_at_least_one_true(self):
        return any(self.bool_list)

if __name__ == '__main__':
    checker_true = BooleanChecker([False, False, True, False])
    result_true = checker_true.check_at_least_one_true()
    print(f"Result for [False, False, True, False]: {result_true}")

    checker_false = BooleanChecker([False, False, False])
    result_false = checker_false.check_at_least_one_true()
    print(f"Result for [False, False, False]: {result_false}")

    checker_all_true = BooleanChecker([True, True, True])
    result_all_true = checker_all_true.check_at_least_one_true()
    print(f"Result for [True, True, True]: {result_all_true}")

    checker_empty = BooleanChecker([])
    result_empty = checker_empty.check_at_least_one_true()
    print(f"Result for []: {result_empty}")