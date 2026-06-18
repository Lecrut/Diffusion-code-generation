class ValueChecker:
    def check_if_zero(self, value):
        """
        Determines if the input value is zero.
        
        Args:
            value (int or float): The numeric value to check.
            
        Returns:
            bool: True if value is 0, False otherwise.
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()
    
    # Hard-coded sample values for testing
    test_values = [0, -1, 1, 0.0, 3.5]
    
    print("Testing check_if_zero method:")
    for val in test_values:
        result = checker.check_if_zero(val)
        status = "Zero" if result else "Not Zero"
        print(f"{val} -> {status}")