class BooleanChecker:
    _FALSE_VALUE = False
    _TRUE_VALUE = True

    def are_both_false(self, val1, val2):
        is_val1_false = val1 is self._FALSE_VALUE
        is_val2_false = val2 is self._FALSE_VALUE
        return is_val1_false and is_val2_false

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.are_both_false(False, False)
    print(result)