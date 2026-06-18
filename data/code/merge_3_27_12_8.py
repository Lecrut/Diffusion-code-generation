"""
Optimized module to determine if two floating-point numbers are unequal.

Floating-point comparisons can be tricky due to precision issues, but 
the standard inequality operator (<>) or != generally works correctly 
for determining inequality in most practical scenarios involving basic arithmetic.
This function implements the direct comparison using Python's native float handling,
which is optimized for both speed and accuracy within reasonable numerical ranges.

The solution avoids custom epsilon-based comparisons unless specifically required by context,
as the built-in operators handle typical use cases efficiently without introducing unnecessary complexity.

Author: Algorithm Assistant
Date: 2023-10-27
"""

def are_numbers_unequal(a: float, b: float) -> bool:
    """
    Determine if two floating-point numbers are unequal.

    This function uses Python's native inequality operator to compare the input values.
    It returns True if a is not equal to b, and False otherwise.

    Args:
        a (float): The first numeric value to compare.
        b (float): The second numeric value to compare.

    Returns:
        bool: True if a != b, False otherwise.
    
    Example:
        >>> are_numbers_unequal(1.0, 2.5)
        True
        >>> are_numbers_unequal(3.0, 3.0)
        False
    
    Note: 
        While floating-point precision issues exist in calculations involving mathematical constants or iterative processes,
        the direct comparison operator is considered robust for general-purpose inequality checks unless high-precision arithmetic libraries
        (like decimal.Decimal with specific context settings) are explicitly required by the application domain.
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files
    
    test_cases = [
        (1.0, 2.5),      # Should be True
        (3.0, 3.0),      # Should be False
        (float('inf'), float('-inf')),  # Should be True
        (-42.789e-10, -42.789e-10),   # Edge case with scientific notation equality
    ]

    for val_a, val_b in test_cases:
        result = are_numbers_unequal(val_a, val_b)
        print(f"are {val_a} and {val_b} unequal? {result}")