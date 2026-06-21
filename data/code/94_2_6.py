class BooleanChecker:
    def has_at_least_one_true(self, boolean_list):
        return any(boolean_list)

if __name__ == '__main__':
    checker = BooleanChecker()
    sample_list = [False, False, True, False]
    result = checker.has_at_least_one_true(sample_list)
    print(result)