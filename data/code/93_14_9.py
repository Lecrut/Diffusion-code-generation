class BooleanChecker:
    FALSE_CONSTANT = False

    @staticmethod
    def verify_false(val1, val2):
        return val1 is BooleanChecker.FALSE_CONSTANT and val2 is BooleanChecker.FALSE_CONSTANT

if __name__ == '__main__':
    sample_value_one = False
    sample_value_two = False
    checker_instance = BooleanChecker()
    computed_result = checker_instance.verify_false(sample_value_one, sample_value_two)
    print(computed_result)