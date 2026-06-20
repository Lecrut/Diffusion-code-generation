class BooleanChecker:
    def check_both_false(self, a: bool, b: bool) -> bool:
        return not a and not b

if __name__ == '__main__':
    checker = BooleanChecker()
    test_cases = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False
    }
    
    for inputs, expected in test_cases.items():
        result = checker.check_both_false(*inputs)
        print(f"check_both_false({inputs[0]}, {inputs[1]}): {result}, Expected: {expected}")