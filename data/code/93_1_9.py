class BooleanChecker:
    @staticmethod
    def are_both_false(a, b):
        return not a and not b

if __name__ == '__main__':
    print(BooleanChecker.are_both_false(False, False))
    print(BooleanChecker.are_both_false(True, False))
    print(BooleanChecker.are_both_false(False, True))
    print(BooleanChecker.are_both_false(True, True))