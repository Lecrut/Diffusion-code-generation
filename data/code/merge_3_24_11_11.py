class NumberChecker:
    def check_negativity(self, value):
        """
        Determines if the provided input is negative.
        
        Handles integers and floating-point numbers. 
        Returns True if less than zero, False otherwise.
        
        Args:
            value (int or float): The number to check.
            
        Returns:
            bool: True if value < 0, else False.
        """
        return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample test cases without user input or file access
    sample_values = [
        -5,
        0,
        -3.14,
        "negative string",
        [],
        {},
        None,
        float('-inf'),
        float('nan')
    ]

    for val in sample_values:
        result = checker.check_negativity(val)
        print(f"Is {val!r} negative? {result}")