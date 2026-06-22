class BooleanChecker:
    _FALSE = False
    _TRUE = True

    @staticmethod
    def _check_values(a, b):
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Inputs must be boolean values")
        return a is BooleanChecker._FALSE and b is BooleanChecker._FALSE

    @staticmethod
    def both_false_generator(a, b):
        yield BooleanChecker._check_values(a, b)

if __name__ == '__main__':
    result1 = list(BooleanChecker.both_false_generator(False, False))
    print(result1)
    result2 = list(BooleanChecker.both_false_generator(True, False))
    print(result2)
    result3 = list(BooleanChecker.both_false_generator(False, True))
    print(result3)
    result4 = list(BooleanChecker.both_false_generator(True, True))
    print(result4)