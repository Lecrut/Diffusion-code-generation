class BooleanChecker:
    _VALUE_TO_FLAG = {False: 0, True: 1}

    def are_both_false(self, val1, val2):
        flag1 = self._VALUE_TO_FLAG.get(val1, -1)
        flag2 = self._VALUE_TO_FLAG.get(val2, -1)
        if flag1 == -1 or flag2 == -1:
            raise ValueError("Inputs must be boolean values")
        return flag1 == 0 and flag2 == 0

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.are_both_false(False, False)
    print(result)