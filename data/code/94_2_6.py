class BooleanChecker:
    def has_at_least_one_true(self, boolean_list):
        return any(boolean_list)

if __name__ == '__main__':
    checker = BooleanChecker()
    sample_values = [False, False, True, False]
    print(checker.has_at_least_one_true(sample_values))