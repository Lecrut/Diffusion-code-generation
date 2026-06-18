class ValueChecker:
    def check_if_zero(self, value):
        """
        Determines if the input value is zero.
        
        Args:
            value (int or float): The number to check
            
        Returns:
            bool: True if value is 0, False otherwise
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()
    
    # Test cases with hard-coded sample values
    test_values = [
        (0.0, "positive float"),
        (-0.0, "negative zero float"),
        (10, "integer greater than zero"),
        (-5, "integer less than zero"),
        ("zero", "string 'zero'"),
        ([], "empty list"),
        ({}, "empty dictionary")
    ]
    
    print("Testing ValueChecker.check_if_zero() method:")
    for value, description in test_values:
        result = checker.check_if_zero(value)
        expected_type_check = isinstance(value, (int, float)) and value == 0
        
        # Note: For non-numeric types or edge cases like empty containers being falsy but not zero-value numerically
        # We strictly check numerical equality for 'zero' determination as per standard math definition
        status = "PASS" if result else f"FALSY ({type(value).__name__}) - Not treated as numeric zero unless int/float is 0"
        
        print(f"{description}: {result} -> Status: {status}")