class BoolChecker:
    @staticmethod
    def check_both_false(a: bool, b: bool) -> bool:
        return not (a | b)

if __name__ == '__main__':
    print(BoolChecker.check_both_false(False, False))
    print(BoolChecker.check_both_false(True, False))
    print(BoolChecker.check_both_false(False, True))
    print(BoolChecker.check_both_false(True, True))