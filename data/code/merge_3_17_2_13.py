class NumberChecker:
    def check_parity(self, number):
        """
        Determines if an integer is even.
        
        Args:
            number (int): The integer to be checked.
            
        Returns:
            bool: True if the number is even, False otherwise.
        """
        return number % 2 == 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    sample_values = [10, 7, -4, 0, 3]
    
    for value in sample_values:
        is_even = checker.check_parity(value)
        print(f"Is {value} even? {is_even}")