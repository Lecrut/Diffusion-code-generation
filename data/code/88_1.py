class BooleanChecker:
    def is_both_true(self, a: bool, b: bool) -> bool:
        return a and b
if __name__ == '__main__':
    checker = BooleanChecker()
    print(f"is_both_true(True, True): {checker.is_both_true(True, True)}")
    print(f"is_both_true(True, False): {checker.is_both_true(True, False)}")
    print(f"is_both_true(False, True): {checker.is_both_true(False, True)}")
    print(f"is_both_true(False, False): {checker.is_both_true(False, False)}")