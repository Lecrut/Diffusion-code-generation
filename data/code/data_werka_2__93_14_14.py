class BooleanChecker:
    FALSE_CONSTANT = False

    @staticmethod
    def verify_false(val):
        return val is BooleanChecker.FALSE_CONSTANT

    @classmethod
    def both_false(cls, first, second):
        return cls.verify_false(first) and cls.verify_false(second)

if __name__ == '__main__':
    sample_flag_1 = False
    sample_flag_2 = False
    outcome = BooleanChecker.both_false(sample_flag_1, sample_flag_2)
    print(outcome)