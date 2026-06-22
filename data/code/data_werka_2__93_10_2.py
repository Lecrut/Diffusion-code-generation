class BooleanChecker:
    _FALSE_MAP = {False: 0, True: 1}

    def are_both_false(self, val1, val2):
        return self._FALSE_MAP.get(val1, 0) == 0 and self._FALSE_MAP.get(val2, 0) == 0

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.are_both_false(False, False)
    print(result)