class NumberChecker:
    def is_even(self, n):
        return not (n % 2)
if __name__ == '__main__':
    checker = NumberChecker()
    test_cases = [0, 1, 2, -3, 4, 5]
    for case in test_cases:
        print(f"{case} is even: {checker.is_even(case)}")