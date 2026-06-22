class BooleanChecker:
    TRUE_FLAG = 1
    FALSE_FLAG = 0

    @staticmethod
    def _to_int(val):
        if val is False:
            return BooleanChecker.FALSE_FLAG
        if val is True:
            return BooleanChecker.TRUE_FLAG
        raise ValueError("Input must be a boolean")

    def are_both_false(self, val1, val2):
        int1 = self._to_int(val1)
        int2 = self._to_int(val2)
        return int1 == self.FALSE_FLAG and int2 == self.FALSE_FLAG

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.are_both_false(False, False)
    print(result)