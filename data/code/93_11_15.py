class BooleanChecker:

    def are_both_false(self, a, b):
        return not a and (not b)
if __name__ == '__main__':
    checker = BooleanChecker()
    sample1 = checker.are_both_false(False, False)
    sample2 = checker.are_both_false(True, False)
    sample3 = checker.are_both_false(False, True)
    sample4 = checker.are_both_false(True, True)
    print(sample1)
    print(sample2)
    print(sample3)
    print(sample4)