class NumberChecker:
    def is_even(self, number):
        return number % 2 == 0
if __name__ == '__main__':
    checker = NumberChecker()
    test_values = [10, -3, 42, 0]
    for val in test_values:
        print(f"{val}: {checker.is_even(val)}")