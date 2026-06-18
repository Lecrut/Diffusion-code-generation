class NumberChecker:
    def check_if_negative(self, value):
        """
        Determines if the input value is negative.

        Args:
            value (int or float): The number to evaluate.

        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values for testing without user input
    test_values = [10, -5, 3.14, 0, -2.5]

    print("Testing check_if_negative method:")
    for val in test_values:
        result = checker.check_if_negative(val)
        status = "negative" if result else "not negative (non-negative)"
        print(f"{val} -> {status}")