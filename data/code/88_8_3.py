class BooleanChecker:
    @staticmethod
    def check_both_true(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    print(BooleanChecker.check_both_true(True, True))
    print(BooleanChecker.check_both_true(False, True))
    print(BooleanChecker.check_both_true(True, False))
    print(BooleanChecker.check_both_true(False, False))