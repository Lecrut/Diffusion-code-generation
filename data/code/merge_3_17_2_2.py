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
    
    # Hard-coded sample values
    test_values = [10, -3, 42, 0, 7]
    
    for value in test_values:
        result = checker.check_parity(value)
        print(f"{value} is {'even' if result else 'odd'}")