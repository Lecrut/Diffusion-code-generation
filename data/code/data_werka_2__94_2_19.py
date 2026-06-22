class BooleanChecker:
    def has_at_least_one_true(self, boolean_list):
        if not isinstance(boolean_list, list):
            raise ValueError("Input must be a list")
        for value in boolean_list:
            if value is True:
                return True
        return False

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.has_at_least_one_true([False, False, True])
    print(result)
    result2 = checker.has_at_least_one_true([False, False, False])
    print(result2)