class NumberChecker:
    def check_if_negative(self, value):
        """
        Determines if the input value is negative.
        
        Args:
            value (int or float): The number to check.
            
        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    test_values = [
        -5,      # Negative integer
        0,       # Zero (not negative)
        3.14,    # Positive float
        -2.718,  # Negative float
        None     # Edge case: will raise TypeError as expected for strict numeric check
    ]
    
    print("Testing NumberChecker.check_if_negative:")
    for val in test_values[:-1]:  # Skip None to avoid error during demo output unless desired
        result = checker.check_if_negative(val)
        status = "Negative" if result else "Non-negative"
        print(f"Value: {val} -> Is Negative? {status}")
    
    # Demonstrate behavior with invalid input (optional, commented out for clean run)
    # try:
    #     res = checker.check_if_negative(None)
    # except TypeError as e:
    #     print(f"None is not a valid number. Error: {e}")