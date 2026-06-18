class NumberChecker:
    def is_even(self, num):
        return bool(num & 1) if isinstance(num, int) else False
if __name__ == '__main__':
    checker = NumberChecker()
    test_cases = [0, -5, 42, 'string', None]
    for case in test_cases:
        print(f"{case}: {checker.is_even(case)}")