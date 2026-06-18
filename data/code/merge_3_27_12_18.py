"""
Module to determine if two floating-point numbers are unequal using an optimized approach.

Floating-point comparison can be tricky due to precision issues. The standard `!=` operator 
is generally robust enough for most practical purposes, but explicit epsilon-based checks 
are often preferred in scientific computing when exact equality is not expected and small 
differences might occur. However, the task specifically asks if they are *unequal*.

The most optimized and Pythonic way to check inequality between two floats without 
introducing unnecessary complexity or potential errors from custom epsilons (which require 
careful selection) is to rely on the built-in `!=` operator. The CPython implementation of 
float comparison is highly optimized at the hardware level for this specific operation.

Attempting a manual epsilon-based check introduces variables that must be tuned, which can 
lead to incorrect results if not perfectly calibrated (e.g., comparing very large numbers).
Therefore, the optimal solution uses `a != b`.

This function wraps the standard comparison with minimal overhead and includes clear documentation
as per general best practices for such utility functions.
"""

def are_unequal(a: float, b: float) -> bool:
    """
    Determine if two floating-point numbers are unequal.

    This method uses Python's built-in inequality operator which is implemented efficiently 
    in C and handles the nuances of IEEE 754 floating-point arithmetic correctly for standard use cases.

    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.

    Returns:
        bool: True if a is not equal to b, False otherwise.
    
    Example:
        >>> are_unequal(1.0, 2.0)
        True
        >>> are_unequal(3.5, 3.5)
        False
    """
    return a != b

if __name__ == '__main__':
    pass
