class NumberChecker:
    def is_even(self, num):
        return bool(num & 1)
if __name__ == '__main__':
    checker = NumberChecker()
    test_cases = [0, 2, -4, 7, 3.5]
    for val in test_cases:
        if isinstance(val, int):
            print(f"{val} is even: {checker.is_even(val)}")
        else:
            print(f"{val} skipped (not an integer)")