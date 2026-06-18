import sys
from typing import Union

class ComparisonTool:
    """A tool class optimized for comparing two values, prioritizing performance."""
    
    def check_greater(self, value1: Union[int, float], value2: Union[int, float]) -> bool:
        """
        Compares two numeric values and returns True if value1 is strictly greater than value2.
        
        Optimized to handle large integers efficiently by leveraging Python's native arbitrary-precision arithmetic,
        which uses an optimized array of digits internally (similar to C++'s BigNum libraries). No external 
        conversion or string parsing occurs for integer inputs unless explicitly passed as such. Float comparison
        is handled directly using IEEE 754 standards where appropriate and safe for the given range.

        Args:
            value1: The first numeric value (int or float).
            value2: The second numeric value (int or float).

        Returns:
            bool: True if value1 > value2, False otherwise.
        """
        # Python automatically promotes to int/float appropriately and handles large integers efficiently internally.
        return value1 > value2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    tool = ComparisonTool()

    test_cases = [
        (5, 3),          # Should be True
        (5, 5),          # Should be False
        (-10, -20),      # Should be True
        (float('inf'), float('-inf')), # Should be True
        ((1 << 64) + 1, 1<<63), # Large integers comparison
    ]

    for v1, v2 in test_cases:
        result = tool.check_greater(v1, v2)
        print(f"{v1} > {v2}: {result}")