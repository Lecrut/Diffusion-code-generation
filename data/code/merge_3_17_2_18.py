class NumberChecker:
    def check_parity(self, number):
        """
        Determines if an integer is even.
        
        Args:
            number (int): The integer to check.
            
        Returns:
            bool: True if the number is even, False otherwise.
        """
        return number % 2 == 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample values for testing without user input or external dependencies
    test_cases = [10, -5, 42, 0, 3]
    
    print("Number Parity Check Results:")
    for num in test_cases:
        is_even = checker.check_parity(num)
        status = "Even" if is_even else "Odd"
        print(f"{num} -> {status}")