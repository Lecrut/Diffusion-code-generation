class TruthChecker:
    @staticmethod
    def check_both_true(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    print(TruthChecker.check_both_true(True, True))
    print(TruthChecker.check_both_true(True, False))
    print(TruthChecker.check_both_true(False, True))
    print(TruthChecker.check_both_true(False, False))