class NumberChecker:
    def is_even(self, num):
        return bool(num & 1)
if __name__ == '__main__':
    checker = NumberChecker()
    test_cases = [0, 2, -4, 3, -5]
    for case in test_cases:
        result = checker.is_even(case)
        print(f"{case} is {'even' if result else 'odd'}")