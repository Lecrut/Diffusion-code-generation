class BooleanChecker:
    def has_at_least_one_true(self, boolean_list):
        for value in boolean_list:
            if value:
                return True
        return False

if __name__ == '__main__':
    checker = BooleanChecker()
    sample1 = [False, False, False]
    sample2 = [True, False, False]
    sample3 = []
    sample4 = [False, False, True, False]
    sample5 = [True]

    print(f"Sample 1: {sample1}, Result: {checker.has_at_least_one_true(sample1)}")
    print(f"Sample 2: {sample2}, Result: {checker.has_at_least_one_true(sample2)}")
    print(f"Sample 3: {sample3}, Result: {checker.has_at_least_one_true(sample3)}")
    print(f"Sample 4: {sample4}, Result: {checker.has_at_least_one_true(sample4)}")
    print(f"Sample 5: {sample5}, Result: {checker.has_at_least_one_true(sample5)}")