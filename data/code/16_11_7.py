class NumberChecker:
    def check_positivity(self, value):
        """
        Determines if the provided numeric value is positive (strictly greater than zero).
        
        Args:
            value: A number to be checked.
            
        Returns:
            bool: True if value > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()

    test_values = [5, -3, 0, 2.718]

    for val in test_values:
        result = checker.check_positivity(val)
        print(f"Is {val} positive? {result}")