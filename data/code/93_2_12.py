class BooleanChecker:
    def check_both_false(self, a: bool, b: bool) -> bool:
        return not a and not b

if __name__ == '__main__':
    checker = BooleanChecker()
    result1 = checker.check_both_false(False, False)
    print(f"check_both_false(False, False): {result1}")