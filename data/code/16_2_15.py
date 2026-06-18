class NumberChecker:
    def check_positivity(self, value):
        """
        Determines if the input value is positive (strictly greater than zero).
        
        Args:
            value: The numeric value to check. Can be int or float.
            
        Returns:
            bool: True if value > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Hard-coded sample values for testing without user input