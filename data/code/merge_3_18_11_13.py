import sys
from typing import Union

class ComparisonTool:
    """A tool class optimized for comparing two values efficiently."""

    def check_greater(self, value1: Union[int, float], value2: Union[int, float]) -> bool:
        """
        Compares two numeric values and returns True if value1 is strictly greater than value2.
        
        This implementation handles large integers directly without converting them to strings 
        or using floating-point arithmetic which can lose precision for very large numbers.
        
        Args:
            value1 (int | float): The first number to compare.
            value2 (int | float): The second number to compare.
            
        Returns:
            bool: True if value1 > value2, False otherwise.
        """
        # Ensure both are numeric types supported for comparison in Python 3
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise TypeError("Both values must be integers or floats.")

        try:
            return value1 > value2
        except OverflowError:
            # In rare cases with extremely large numbers in some environments, 
            # though Python handles arbitrary precision ints well.
            return False

if __name__ == '__main__':
    tool = ComparisonTool()

    # Hard-coded sample values for testing without user input or network access
    samples = [
        (10**50 + 7, 10**50),      # Large integers comparison
        (-42.5, -38.9),            # Negative floats with high precision needed conceptually
        (float('inf'), float('-inf')), # Infinity comparisons
        (True, False),              # Note: bool is subclass of int in Python
    ]

    for val1, val2 in samples:
        result = tool.check_greater(val1, val2)
        print(f"{val1} > {val2}: {result}")