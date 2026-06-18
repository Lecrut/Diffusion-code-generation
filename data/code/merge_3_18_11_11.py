import sys
from typing import Union

class ComparisonTool:
    """A tool class optimized for comparing two values efficiently."""
    
    def check_greater(self, value1: Union[int, float], value2: Union[int, float]) -> bool:
        """
        Compares two numeric values and returns True if value1 is strictly greater than value2.
        
        Optimized to handle large integers by leveraging Python's native arbitrary-precision 
        integer arithmetic which is implemented in C for speed. Floating-point comparisons
        are handled using standard IEEE 754 semantics, optimized via direct operator usage.
        
        Args:
            value1 (int | float): The first numeric value.
            value2 (int | float): The second numeric value.
            
        Returns:
            bool: True if value1 > value2, False otherwise.
        """
        # Direct comparison is the most optimized approach in Python for both int and float
        return value1 > value2

if __name__ == '__main__':
    tool = ComparisonTool()
    
    # Hard-coded sample values including large integers to test performance optimization claims
    samples = [
        (45, 30),           # Standard case: True
        (-10, -5),          # Negative numbers: False
        (2.718, 2.719),     # Floating point precision check: False
        (1 << 60 + 1, 1 << 60), # Very large integers optimized via native C implementation
    ]

    for v1, v2 in samples:
        result = tool.check_greater(v1, v2)
        print(f"{v1} > {v2}: {result}")