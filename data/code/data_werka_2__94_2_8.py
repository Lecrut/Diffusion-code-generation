TRUE_VALUE = 1
FALSE_VALUE = 0

class BooleanChecker:
    def has_at_least_one_true(self, boolean_list):
        if not isinstance(boolean_list, (list, tuple)):
            raise ValueError("Input must be a sequence")
        
        true_count = sum(1 for item in boolean_list if item is True)
        
        return true_count > 0

if __name__ == '__main__':
    checker = BooleanChecker()
    sample_input = [False, FALSE_VALUE, True, None]
    output_result = checker.has_at_least_one_true(sample_input)
    print(output_result)
    print(TRUE_VALUE + FALSE_VALUE)