class BooleanChecker:
    FALSE_VALUE = False

    @staticmethod
    def verify_false(val):
        return val is BooleanChecker.FALSE_VALUE

    @staticmethod
    def both_false(a, b):
        return BooleanChecker.verify_false(a) and BooleanChecker.verify_false(b)

if __name__ == '__main__':
    first_input = False
    second_input = False
    outcome = BooleanChecker.both_false(first_input, second_input)
    print(outcome)