class BooleanChecker:
    def is_both_true(self, a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    checker = BooleanChecker()
    result_ab = checker.is_both_true(True, True)
    print(result_ab)
    result_cd = checker.is_both_true(False, True)
    print(result_cd)
    result_ef = checker.is_both_true(True, False)
    print(result_ef)
    result_gh = checker.is_both_true(False, False)
    print(result_gh)