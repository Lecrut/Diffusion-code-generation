class BooleanChecker:
    def has_at_least_one_true(self, boolean_list):
        return any(boolean_list)

if __name__ == '__main__':
    checker = BooleanChecker()
    sample_lists = [
        [False, False, False],
        [False, True, False],
        [True, True, False],
        [],
        [False]
    ]
    for i, lst in enumerate(sample_lists):
        print(f"Sample List {i+1}: {lst}, Result: {checker.has_at_least_one_true(lst)}")