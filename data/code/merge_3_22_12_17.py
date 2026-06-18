class NumberChecker:
    def check_odd(self, number):
        """Returns True if 'number' is odd, False otherwise."""
        return bool(number % 2)

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    test_values = [7, 10, -3, 0]
    
    for value in test_values:
        result = checker.check_odd(value)
        print(f"Is {value} odd? {result}")