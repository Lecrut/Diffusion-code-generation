class NumberChecker:
    def check_if_negative(self, value):
        """
        Determines if the given numeric value is negative.
        
        Args:
            value (int or float): The number to be checked.
            
        Returns:
            bool: True if value is less than zero, False otherwise.
        """
        return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Hard-coded sample values to test the method without user input
    samples = [-5, -3.14, 0, 2, 1e-8]

    for sample in samples:
        result = checker.check_if_negative(sample)
        print(f"{sample} is negative: {result}")