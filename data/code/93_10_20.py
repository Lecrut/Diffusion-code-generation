class BooleanChecker:
    _VALID_TYPES = (bool,)

    def are_both_false(self, val1, val2):
        if type(val1) not in self._VALID_TYPES or type(val2) not in self._VALID_TYPES:
            raise ValueError("Inputs must be boolean values")
        return val1 is False and val2 is False

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.are_both_false(False, False)
    print(result)