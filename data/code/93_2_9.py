class BooleanChecker:
    def check_both_false(self, a: bool, b: bool) -> bool:
        return not a and not b

if __name__ == '__main__':
    checker = BooleanChecker()
    results = {
        (False, False): checker.check_both_false(False, False),
        (False, True): checker.check_both_false(False, True),
        (True, False): checker.check_both_false(True, False),
        (True, True): checker.check_both_false(True, True)
    }
    for inputs, result in results.items():
        print(f"check_both_false{inputs}: {result}")