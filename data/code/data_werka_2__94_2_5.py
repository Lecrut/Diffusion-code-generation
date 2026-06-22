class BooleanChecker:
    def __init__(self):
        self._true_value = True

    def has_at_least_one_true(self, boolean_list):
        if not hasattr(boolean_list, '__iter__'):
            raise ValueError("Input must be iterable")
        
        result = False
        for item in boolean_list:
            if item is self._true_value:
                result = True
                break
        
        return result

if __name__ == '__main__':
    checker = BooleanChecker()
    sample_data = [False, False, True, False]
    output = checker.has_at_least_one_true(sample_data)
    print(output)