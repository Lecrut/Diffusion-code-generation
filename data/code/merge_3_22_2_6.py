class NumberChecker:
    def check_odd(self, number):
        """
        Returns True if the given integer is odd, False otherwise.
        
        Args:
            number (int): The integer to be checked.
            
        Returns:
            bool: True if 'number' is odd, False otherwise.
        """
        return number % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample test cases with hard-coded values
    test_values = [1, 2, -3, 0, 5]

    for value in test_values:
        result = checker.check_odd(value)
        print(f"Is {value} odd? {result}")