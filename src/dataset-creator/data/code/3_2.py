class NumberChecker:
    def is_even(self, num):
        return not (num % 2)
if __name__ == '__main__':
    checker = NumberChecker()
    test_cases = [10, -4, 7, 3.5]
    for case in test_cases:
        result = "Even" if checker.is_even(case) else "Odd or Invalid"
        print(f"{case}: {result}")