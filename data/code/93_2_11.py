class BooleanChecker:
    def check_both_false(self, a: bool, b: bool) -> bool:
        return not (a or b)

if __name__ == '__main__':
    checker = BooleanChecker()
    print(f"check_both_false(False, False): {checker.check_both_false(False, False)}")
    print(f"check_both_false(False, True): {checker.check_both_false(False, True)}")
    print(f"check_both_false(True, False): {checker.check_both_false(True, False)}")
    print(f"check_both_false(True, True): {checker.check_both_false(True, True)}")