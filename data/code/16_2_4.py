class NumberChecker:
    def check_positivity(self, value):
        """
        Determines if the input value is positive (strictly greater than zero).

        Args:
            value: The number to evaluate. Can be int or float.

        Returns:
            bool: True if value > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values covering various cases
    test_values = [5, -3, 0, 2.718, -4.5]

    for val in test_values:
        result = checker.check_positivity(val)
        print(f"Is {val} positive? {result}")