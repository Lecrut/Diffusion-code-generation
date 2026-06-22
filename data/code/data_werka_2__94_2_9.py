class BooleanChecker:
    def has_at_least_one_true(self, boolean_list):
        if not isinstance(boolean_list, list):
            raise ValueError("Input must be a list")
        return any(boolean_list)

if __name__ == '__main__':
    checker = BooleanChecker()
    sample_data = [False, False, False, False]
    sample_data_with_true = [False, False, True, False]
    empty_data = []
    result1 = checker.has_at_least_one_true(sample_data)
    result2 = checker.has_at_least_one_true(sample_data_with_true)
    result3 = checker.has_at_least_one_true(empty_data)
    print(result1)
    print(result2)
    print(result3)