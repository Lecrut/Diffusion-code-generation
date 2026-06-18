import sys

class ComparisonTool:
    """A utility class to compare two values efficiently."""

    def check_greater(self, a, b):
        """
        Compare two values and return True if 'a' is strictly greater than 'b', False otherwise.

        This method uses the most efficient comparison operator for Python's data types,
        which leverages C-level optimizations under the hood rather than manual branching logic.

        Args:
            a (any): The first value to compare.
            b (any): The second value to compare.

        Returns:
            bool: True if 'a' > 'b', False otherwise.
        """
        return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    tool = ComparisonTool()

    # Test cases with various data types (integers, floats, strings) to ensure broad compatibility
    test_cases = [
        ("integer greater", 10, 5),       # Expected: True
        ("integer equal", 7, 7),          # Expected: False
        ("string less", "apple", "banana"), # Expected: True
        ("float comparison", 3.14, 2.71), # Expected: True
    ]

    for description, val_a, val_b in test_cases:
        result = tool.check_greater(val_a, val_b)
        print(f"{description}: {val_a} > {val_b} is {result}")