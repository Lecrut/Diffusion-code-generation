class LengthCalculator:
    """A class to perform calculations involving lengths."""

    def get_ratio(self, a: float, b: float) -> float:
        """Calculates the ratio of length 'a' to length 'b'.
        
        Args:
            a (float): The first length value.
            b (float): The second length value. If zero, raises ZeroDivisionError.

        Returns:
            float: The result of dividing 'a' by 'b'.

        Raises:
            ValueError: If either input is not numeric.
            ZeroDivisionError: If the denominator ('b') is zero.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both inputs must be numbers.")

        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero length.")

        return a / b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files.
    calc = LengthCalculator()
    
    try:
        result1 = calc.get_ratio(10, 5)
        print(f"Ratio of {10} to {5}: {result1}")

        result2 = calc.get_ratio(-4, 8)
        print(f"Ratio of {-4} to {8}: {result2}")

        # Test edge case: zero denominator
        try:
            _ = calc.get_ratio(10, 0)
        except ZeroDivisionError as e:
            print(f"Expected error for division by zero: {e}")

    except ValueError as ve:
        print(f"Value Error encountered: {ve}")