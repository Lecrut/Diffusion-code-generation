class NumberChecker:
    def check_if_negative(self, value):
        """
        Determines if a given numeric input is negative.
        
        Parameters:
            value (int or float): The number to be checked.
            
        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    checker = NumberChecker()

    test_values = [10, -5.7, 0, None, "string"]

    for val in test_values:
        result = checker.check_if_negative(val)
        print(f"Is {val} negative? {result}")