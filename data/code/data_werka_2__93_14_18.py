class BooleanChecker:
    FALSE_CONSTANT = False

    @staticmethod
    def are_both_false(val_a, val_b):
        return val_a == BooleanChecker.FALSE_CONSTANT and val_b == BooleanChecker.FALSE_CONSTANT

if __name__ == '__main__':
    sample_a = False
    sample_b = False
    result = BooleanChecker.are_both_false(sample_a, sample_b)
    print(result)