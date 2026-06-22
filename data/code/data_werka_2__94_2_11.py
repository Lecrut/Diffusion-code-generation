class BooleanChecker:
    TRUE_SENTINEL = True
    FALSE_SENTINEL = False

    @staticmethod
    def _validate_input(boolean_list):
        if not isinstance(boolean_list, (list, tuple)):
            raise ValueError("Input must be a list or tuple")
        for item in boolean_list:
            if not isinstance(item, bool):
                raise ValueError("All items must be boolean values")

    def has_at_least_one_true(self, boolean_list):
        self._validate_input(boolean_list)
        return any(boolean_list)

if __name__ == '__main__':
    checker = BooleanChecker()
    sample_data = [False, False, True, False]
    output = checker.has_at_least_one_true(sample_data)
    print(output)