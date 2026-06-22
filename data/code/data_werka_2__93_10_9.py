class BooleanChecker:
    _FALSE_VALUE = False
    _TRUE_VALUE = True

    @staticmethod
    def _is_false(val):
        return val is BooleanChecker._FALSE_VALUE

    def are_both_false(self, val1, val2):
        return BooleanChecker._is_false(val1) and BooleanChecker._is_false(val2)

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.are_both_false(False, False)
    print(result)