class NumberChecker:
    """A class to perform basic number checks."""
    
    def check_parity(self, n):
        """
        Determines if an integer is even or odd.
        
        Args:
            n (int): The integer to be checked.
            
        Returns:
            bool: True if the number is even, False otherwise.
        """
        return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [10, -3, 42, 0, 7]

    checker = NumberChecker()

    print("Testing parity of numbers:")
    for num in test_values:
        is_even = checker.check_parity(num)
        status = "Even" if is_even else "Odd"
        print(f"{num} -> {status}")