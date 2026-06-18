class LengthCalculator:
    """A class to perform calculations involving lengths."""

    def get_ratio(self, a, b):
        """
        Calculates the ratio of length 'a' to length 'b'.

        Args:
            a (int | float): The numerator length.
            b (int | float): The denominator length. Must not be zero.

        Returns:
            float: The calculated ratio if successful, otherwise raises ValueError or ZeroDivisionError.
        
        Raises:
            ValueError: If 'b' is None or non-numeric.
            ZeroDivisionError: If 'b' is 0.
        """
        try:
            a = float(a)
            b = float(b)
            
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
                
            return a / b
        except TypeError as e:
            raise ValueError(f"Inputs must be numeric. Error occurred: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to test the class functionality without user input.
    calculator = LengthCalculator()

    # Test case 1: Simple positive ratio
    result_1 = calculator.get_ratio(10, 5)
    
    # Test case 2: Ratio with decimals and larger numbers
    result_2 = calculator.get_ratio(1734.56, 89.2)

    # Test case 3: Negative ratio
    result_3 = calculator.get_ratio(-10, 5)

    print(f"Ratio of {10} to {5}: {result_1}")
    print(f"Ratio of {1734.56} to {89.2}: {result_2}")
    print(f"Ratio of {-10} to {5}: {result_3}")

    # Demonstrate error handling (optional internal check, not printed)
    try:
        calculator.get_ratio(10, 0)
    except ZeroDivisionError as e:
        print(f"Caught expected error for zero denominator: {e}")