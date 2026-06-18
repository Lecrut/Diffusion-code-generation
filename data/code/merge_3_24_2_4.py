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
    
    # Sample values for testing without user input or external dependencies
    test_values = [10, -5, 0.0, -3.14, 2]
    
    print("Testing check_if_negative method:")
    for val in test_values:
        result = checker.check_if_negative(val)
        status = "Negative" if result else "Non-negative or zero"
        print(f"{val} -> {status}")