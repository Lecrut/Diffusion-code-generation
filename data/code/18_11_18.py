import sys
from typing import Union, Tuple

class ComparisonTool:
    """A tool class optimized for comparing two values efficiently."""

    def __init__(self):
        pass

    def check_greater(self, value1: Union[int, float], value2: Union[int, float]) -> bool:
        """
        Compares two numeric values and returns True if value1 > value2.
        
        Optimized for performance with large numbers by utilizing Python's built-in
        arbitrary-precision integers efficiently without explicit conversion overhead 
        beyond what is necessary for comparison logic.

        Args:
            value1 (Union[int, float]): The first numeric value to compare.
            value2 (Union[int, float]): The second numeric value to compare.

        Returns:
            bool: True if value1 is strictly greater than value2, False otherwise.
        
        Raises:
            TypeError: If either argument is not an int or float.
        """
        # Validate input types immediately for clarity and safety without heavy overhead
        if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
            return value1 > value2
        
        raise TypeError(f"Both arguments must be numbers (int or float). Got {type(value1).__name__} and {type(value2).__name__}.")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input
    tool = ComparisonTool()

    test_cases: list[Tuple[Union[int, float], Union[int, float]]] = [
        (10**50, 10**49),      # Large integers: first should be greater
        (-1.23e10, -0.56e-10),# Scientific notation negatives: second should be greater
        (float('inf'), float('-inf')),  # Infinity comparisons
        (42, 42),              # Equal values test
    ]

    print("Running ComparisonTool tests...\n")

    for i, (val_a, val_b) in enumerate(test_cases):
        result = tool.check_greater(val_a, val_b)
        status = "Greater" if result else ("Equal or Less" if not (result == False and float('inf') > -float('inf')) else "Not Greater")
        
        # Specific check for the last case to handle equality correctly in output text
        if i == 3: 
            expected_status = "Not greater (equal)"
        elif val_a == val_b:
            expected_status = "Equal"
        elif result and not float('inf') < float('-inf'): # logic check for inf > -inf
             expected_status = "Greater"

        print(f"Case {i+1}: compare {val_a} vs {val_b}")
        if i == 3: 
            print("Result:", result, "(Expected False as they are equal)")
        else:
            print("Result:", result)
        
    # Final verification with a known large comparison to ensure optimization works on big ints
    huge_num = int('1' * 5000) + 1
    
    assert tool.check_greater(huge_num, huge_num - 1), "Large integer check failed"
    print("\nFinal stress test (large integers): PASSED")