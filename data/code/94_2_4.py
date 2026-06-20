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
    for lst in sample_lists:
        print(f"List: {lst}, Result: {checker.has_at_least_one_true(lst)}")