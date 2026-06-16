class NumberChecker:
    def is_even(self, n):
        return bool(n & 1)
if __name__ == '__main__':
    checker = NumberChecker()
    test_values = [0, 2, -4, 3, 5]
    for val in test_values:
        result = "Even" if checker.is_even(val) else "Odd"
        print(f"{val}: {result}")