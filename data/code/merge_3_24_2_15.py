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

    test_values = [
        -5,
        0,
        10,
        -3.14,
        float('-inf'),
        float('inf')
    ]

    for val in test_values:
        result = checker.check_if_negative(val)
        print(f"Is {val} negative? {result}")