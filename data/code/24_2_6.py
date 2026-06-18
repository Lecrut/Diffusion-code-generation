class NumberChecker:
    def check_if_negative(self, value):
        """
        Determines if the input value is negative.
        
        Args:
            value (int or float): The number to check.
            
        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample values to test without user input or file access
    test_values = [10, -5, 0, 3.14, -2.718]

    for val in test_values:
        result = checker.check_if_negative(val)
        print(f"Is {val} negative? {result}")