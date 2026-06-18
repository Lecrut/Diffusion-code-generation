class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample test cases with hard-coded values
    samples = [17, -5, 42, 0, 3]

    for num in samples:
        result = checker.check_odd(num)
        print(f"Is {num} odd? {result}")