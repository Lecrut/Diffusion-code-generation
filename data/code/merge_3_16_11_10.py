class NumberChecker:
    """A class designed to check properties of numbers."""

    def check_positivity(self, value):
        """
        Efficiently determines if the provided numeric value is positive.

        A number is considered positive if it is strictly greater than zero.
        Zero and negative numbers return False. Non-numeric types raise a TypeError.

        Args:
            value (int or float): The numerical value to check.

        Returns:
            bool: True if the value is positive, False otherwise.

        Raises:
            TypeError: If 'value' is not an instance of int or float.
        """
        if isinstance(value, (int, float)):
            return value > 0
        else:
            raise TypeError(f"Unsupported type '{type(value).__name__}'. Expected int or float.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    checker = NumberChecker()

    test_cases = [5, -3, 0, 2.718, False]
    
    print("Testing NumberChecker.check_positivity():")
    for val in test_cases:
        try:
            result = checker.check_positivity(val)
            status = "Positive" if result else "Non-positive (Zero or Negative)"
            # Special handling for boolean to avoid calling check_positivity(False/True which are technically 0/-1 numerically 
            # but represent booleans in the input list. We convert them back to int logic: False=0, True=1.
            if isinstance(val, bool):
                result = checker.check_positivity(int(val))
                status = "Positive (as Integer)" if result else "Non-positive"
            print(f"Value {val}: {status}")
        except TypeError as e:
            print(f"Error with value {val}: {e}")