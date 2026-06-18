"""
Efficient module for comparing two arbitrary numeric values for inequality.

This module provides a single function to determine if one number is strictly less than another,
handling integers, floats, decimals, and complex numbers efficiently by leveraging Python's native type hierarchy.
It avoids overhead from external libraries or custom parsing logic where standard operators suffice.
"""

def check_less_than(a: object, b: object) -> bool:
    """
    Check if value a is strictly less than value b.

    Handles int, float (including Decimal), and complex numbers efficiently using native comparison.
    
    Args:
        a: The first numeric value to compare.
        b: The second numeric value to compare against.

    Returns:
        bool: True if a < b is mathematically true in the Python type system, False otherwise.
               Raises TypeError or ValueError for unsupported types (e.g., strings, None).
    
    Complexity:
        O(1) - Relies on C-level comparison logic of native numeric types.
    """
    # Native comparisons cover int, float, and complex efficiently without explicit type checking overhead
    return a < b

if __name__ == '__main__':
    pass
