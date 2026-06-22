class BooleanChecker:
    _STATUS_MAP = {
        True: "true_found",
        False: "no_true"
    }

    def has_at_least_one_true(self, boolean_list):
        if not isinstance(boolean_list, (list, tuple)):
            raise ValueError("Input must be a list or tuple")
        
        for item in boolean_list:
            if item is True:
                return True
        return False

if __name__ == '__main__':
    checker = BooleanChecker()
    test_data = [False, False, False]
    result = checker.has_at_least_one_true(test_data)
    print(result)