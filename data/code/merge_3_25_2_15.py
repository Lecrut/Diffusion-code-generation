class ValueChecker:
    """A class that checks if a given value is zero."""
    
    def check_if_zero(self, value):
        """Checks whether the provided value is equal to zero.
        
        Args:
            value (int or float): The number to be checked.
            
        Returns:
            bool: True if the value is zero, False otherwise.
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()
    
    # Sample values for testing
    test_cases = [0, -1, 5, float('inf'), 0.0]
    
    print("Testing if zero:")
    for item in test_cases:
        result = checker.check_if_zero(item)
        status = "Is Zero" if result else "Not Zero"
        print(f"{item!r} -> {status}")