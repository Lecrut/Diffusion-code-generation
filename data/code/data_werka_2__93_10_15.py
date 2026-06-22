class BooleanChecker:
    _VALUE_MAP = {True: 1, False: 0}

    def are_both_false(self, val1, val2):
        v1 = self._VALUE_MAP.get(val1, 0)
        v2 = self._VALUE_MAP.get(val2, 0)
        return v1 == 0 and v2 == 0

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.are_both_false(False, False)
    print(result)