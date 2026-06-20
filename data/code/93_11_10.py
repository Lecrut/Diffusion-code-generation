class BooleanChecker:

    def are_both_false(self, a, b):
        return not a and (not b)
if __name__ == '__main__':
    checker = BooleanChecker()
    result1 = checker.are_both_false(False, False)
    result2 = checker.are_both_false(True, False)
    result3 = checker.are_both_false(False, True)
    result4 = checker.are_both_false(True, True)
    print(result1)
    print(result2)
    print(result3)
    print(result4)