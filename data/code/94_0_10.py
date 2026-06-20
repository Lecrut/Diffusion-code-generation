class BooleanChecker:
    def __init__(self, bool_list):
        self.bool_list = bool_list

    def check_at_least_one_true(self):
        return any(self.bool_list)

if __name__ == '__main__':
    sample_list_true = [False, False, True, False]
    sample_list_false = [False, False, False]
    sample_list_all_true = [True, True, True]
    sample_list_empty = []

    checker = BooleanChecker(sample_list_true)
    print(f"Result for {sample_list_true}: {checker.check_at_least_one_true()}")

    checker = BooleanChecker(sample_list_false)
    print(f"Result for {sample_list_false}: {checker.check_at_least_one_true()}")

    checker = BooleanChecker(sample_list_all_true)
    print(f"Result for {sample_list_all_true}: {checker.check_at_least_one_true()}")

    checker = BooleanChecker(sample_list_empty)
    print(f"Result for {sample_list_empty}: {checker.check_at_least_one_true()}")