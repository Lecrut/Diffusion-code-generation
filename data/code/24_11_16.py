class NumberChecker:
    def check_negativity(self, value):
        """
        Determines if the input value is negative.
        
        Args:
            value (int or float): The number to check.
            
        Returns:
            bool: True if value < 0, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Hard-coded sample values for testing without user input or arguments
    test_values = [10, -5, 0.0, -3.14, 2]

    print("Testing check_negativity method:")
    for val in test_values:
        result = checker.check_negativity(val)
        status = "Negative" if result else "Non-negative (zero or positive)"
        print(f"{val} -> {status}")