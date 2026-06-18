class ConditionChecker:
    """A class that checks divisibility between two numbers."""

    def check(self, dividend: int | float, divisor: int) -> bool:
        """
        Checks if the first number is divisible by the second number.

        Args:
            dividend (int or float): The number to be divided.
            divisor (int): The number to divide by. Must not be zero.

        Returns:
            bool: True if divisible, False otherwise.

        Raises:
            ValueError: If divisor is zero.
            TypeError: If inputs are of unsupported types for the operation logic intended here.
        """
        # Best-practice error handling for division by zero and type validation
        if not isinstance(divisor, int):
            raise TypeError("Divisor must be an integer.")

        if divisor == 0:
            raise ValueError("Division by zero is undefined.")

        return dividend % divisor == 0

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    checker = ConditionChecker()

    test_cases = [
        (10, 2),   # Expected: True
        (15, 3),   # Expected: True
        (7, 2),    # Expected: False
        (0, 5),    # Expected: True (0 is divisible by any non-zero number)
    ]

    for val1, val2 in test_cases:
        try:
            result = checker.check(val1, val2)
            print(f"{val1} % {val2} == {'True' if result else 'False'}")
        except ValueError as ve:
            print(f"Error with inputs ({val1}, {val2}): Division by zero error - {ve}")
        except TypeError as te:
            print(f"Error with inputs ({val1}, {val2}): Type mismatch - {te}")

    # Test the division by zero case specifically to demonstrate error handling.
    try:
        result = checker.check(5, 0)
    except ValueError:
        print("Correctly caught division by zero exception.")