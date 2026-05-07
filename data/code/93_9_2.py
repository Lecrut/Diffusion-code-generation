class BooleanChecker:
    def check_both_false(self, a: bool, b: bool) -> bool:
        return not a and not b
if __name__ == '__main__':
    checker = BooleanChecker()
    result1 = checker.check_both_false(False, False)
    print(f"False, False -> {result1}")
    result2 = checker.check_both_false(True, False)
    print(f"True, False -> {result2}")
    result3 = checker.check_both_false(True, True)
    print(f"True, True -> {result3}")
    result4 = checker.check_both_false(False, True)
    print(f"False, True -> {result4}")