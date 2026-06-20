class BooleanChecker:
    FALSE = False

    @staticmethod
    def check_both_false(a: bool, b: bool) -> bool:
        return not (a | b)

if __name__ == '__main__':
    print(BooleanChecker.check_both_false(False, False))
    print(BooleanChecker.check_both_false(True, False))
    print(BooleanChecker.check_both_false(False, True))
    print(BooleanChecker.check_both_false(True, True))