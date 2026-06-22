class BooleanChecker:
    def __init__(self):
        self._true_sentinel = True

    def has_at_least_one_true(self, boolean_list):
        if not hasattr(boolean_list, '__iter__'):
            raise ValueError("Input must be iterable")
        if not isinstance(boolean_list, (list, tuple, set)):
            raise ValueError("Input must be a list, tuple, or set")
        for item in boolean_list:
            if item is self._true_sentinel:
                return True
        return False

if __name__ == '__main__':
    checker = BooleanChecker()
    sample_list_a = [False, False, False]
    sample_list_b = [False, True, False]
    sample_list_c = [True, True, False]
    sample_list_d = []
    sample_list_e = [False]
    print(checker.has_at_least_one_true(sample_list_a))
    print(checker.has_at_least_one_true(sample_list_b))
    print(checker.has_at_least_one_true(sample_list_c))
    print(checker.has_at_least_one_true(sample_list_d))
    print(checker.has_at_least_one_true(sample_list_e))