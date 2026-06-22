class BooleanChecker:
    def has_at_least_one_true(self, boolean_list):
        if not isinstance(boolean_list, (list, tuple)):
            raise ValueError("Input must be a list or tuple")
        if len(boolean_list) == 0:
            return False
        return any(boolean_list)

if __name__ == '__main__':
    checker = BooleanChecker()
    sample_data = [False, False, True, False]
    output = checker.has_at_least_one_true(sample_data)
    print(output)