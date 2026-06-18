class ComparisonUtils:
    """Utility class providing comparison methods."""

    @classmethod
    def check_if_greater(cls, value1, value2):
        """
        Compare two arguments to determine if value1 is strictly greater than value2.

        This method supports both primitive types (integers and floats) 
        for a direct numeric comparison using the '>' operator. It returns True 
        if value1 > value2, False otherwise. While object-oriented best practices 
        emphasize extensibility and encapsulation, this specific task is defined as simple,
        so it avoids complex duck-typing introspection to maintain clarity and performance,
        adhering directly to the requirement of checking 'if greater' for standard types.

        Args:
            value1 (int | float): The first numeric argument to compare.
            value2 (int | float): The second numeric argument to compare.

        Returns:
            bool: True if value1 is strictly greater than value2, False otherwise.

        Raises:
            TypeError: If neither input is an int or a float.
        """
        # Ensure both arguments are compatible for comparison (int or float)
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise TypeError("Both values must be integers or floats.")

        return value1 > value2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    
    test_cases = [
        (5, 3),      # Should return True
        (3, 5),      # Should return False
        (7.8, 7.2),  # Should return True
        (-10, -2),   # Should return False (since -10 is less than -2)
    ]

    instance = ComparisonUtils()

    for val1, val2 in test_cases:
        result = instance.check_if_greater(val1, val2)
        print(f"{val1} > {val2}? Result: {result}")