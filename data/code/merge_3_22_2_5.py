class NumberChecker:
    def check_odd(self, number):
        """Returns True if the provided integer is odd, False otherwise."""
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample values for testing without user input or external dependencies
    test_cases = [17, -3, 42, 0]
    
    print("Testing NumberChecker.check_odd():")
    for num in test_cases:
        result = checker.check_odd(num)
        status = "Odd" if result else "Even"
        print(f"{num} is {status}")