class OddChecker:
    def is_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = OddChecker()
    test_values = [17, 24, -5, 8]
    for value in test_values:
        result = checker.is_odd(value)
        print(f"Is {value} odd? {result}")