class NumberChecker:
    def check_odd(self, number: int) -> bool:
        """Returns True if 'number' is odd, False otherwise."""
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    test_values = [5, -3, 10, 0]
    
    for value in test_values:
        result = checker.check_odd(value)
        print(f"Is {value} odd? {result}")