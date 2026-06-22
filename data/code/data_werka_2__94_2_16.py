class BooleanChecker:
    def _validate_input(self, boolean_list):
        if not isinstance(boolean_list, list):
            raise ValueError("Input must be a list")
        for item in boolean_list:
            if not isinstance(item, bool):
                raise ValueError("All items must be boolean")

    def has_at_least_one_true(self, boolean_list):
        self._validate_input(boolean_list)
        return any(boolean_list)

if __name__ == '__main__':
    checker = BooleanChecker()
    sample1 = [False, False, False]
    sample2 = [False, True, False]
    sample3 = []
    result1 = checker.has_at_least_one_true(sample1)
    result2 = checker.has_at_least_one_true(sample2)
    result3 = checker.has_at_least_one_true(sample3)
    print(result1)
    print(result2)
    print(result3)