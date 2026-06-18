class NumberChecker:
    def check_odd(self, number):
        """Returns True if the given integer is odd, False otherwise."""
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    test_cases = [17, 42, -3, 0, 5]
    
    for num in test_cases:
        result = checker.check_odd(num)
        print(f"Is {num} odd? {result}")