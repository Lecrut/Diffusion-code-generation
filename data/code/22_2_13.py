class NumberChecker:
    def check_odd(self, number):
        """Returns True if 'number' is odd, False otherwise."""
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test values with expected results
    test_cases = [17, 42, -3, 0]
    
    for num in test_cases:
        result = checker.check_odd(num)
        print(f"Is {num} odd? {result}")