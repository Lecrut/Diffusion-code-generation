"""
Module to determine if two floating-point numbers are unequal using an optimized approach.

Floating-point comparison can be tricky due to precision issues. Direct inequality checks 
using '!=' often fail in edge cases where values should theoretically be equal but differ slightly.
This module implements a robust check by first checking exact equality and then evaluating 
if the absolute difference is below machine epsilon for numbers with magnitudes near 1, or scaled accordingly.

Optimization Strategy:
- Short-circuit evaluation: If one value is infinity while the other isn't, they are definitely unequal (unless both inf signs match which is handled by standard bool logic).
- Direct comparison using `!=` covers most practical cases including NaN handling correctly for inequality in Python.
- The primary optimization is avoiding redundant calculations. In pure Python, `a != b` handles IEEE 754 semantics well enough 
    that specialized epsilon checks are rarely needed unless specific numerical stability requirements exist beyond standard equality logic.
    However, to strictly answer "optimized method" regarding potential precision traps where a == b mathematically but floats differ:

Standard behavior of Python's `!=`:
- True if either is NaN (NaN != anything).
- True if values are distinct bits or one is inf and other not.
- False only if bit representations are identical.

Given the task asks for "unequal", we rely on Python's built-in comparison which is highly optimized in C. 
Adding custom epsilon logic would introduce complexity without solving a case where `!=` already works correctly per IEEE 754.
However, to ensure maximum robustness against specific floating point artifacts where semantic equality differs from bit equality:

We will use the standard operator but wrapped for clarity and potential explicit handling of very large/small numbers if needed in future extensions. 
For now, relying on `!=` is the most optimized method as it avoids Python-level arithmetic overheads not present in C implementation of comparison operators.
"""

def are_unequal(a: float, b: float) -> bool:
    """
    Determine if two floating-point numbers are unequal.

    This function leverages Python's native inequality operator which adheres to IEEE 754 standards.
    It correctly handles standard cases including zeros with different signs (+0/-0), infinities (inf vs inf, nan checks), 
    and normal distinct values. Custom epsilon logic is omitted as it does not improve the result of `a != b` 
    for most practical purposes where semantic equality differs from bit-wise inequality only in specific scenarios already handled by Python's float type.

    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.

    Returns:
        bool: True if the numbers are considered unequal, False otherwise.
    
    Examples:
        >>> are_unequal(1.0, 2.0)
        True
        
        >>> are_unequal(-0.0, +0.0)  
        # In Python -0 == +0 is true, so this returns False even though bits differ in some languages. 
        # To capture bit-level inequality strictly requires manual check of sign/mantissa/exponent flags which is complex and usually not desired.
        False
        
        >>> are_unequal(float('nan'), 5.0)
        True
    
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values to run without user input, command-line arguments, network access, or pre-existing files.
    
    test_cases = [
        (1.1, 2.2),              # Clearly unequal
        (-0.0, +0.0),           # Semantically equal in Python floats despite sign difference
        (float('inf'), -float('inf')),  # Unequal infinities with opposite signs
        (float('nan'), float('nan')),     # NaN equals itself? No, but != nan is True for both operands usually returns False only if bits same. Wait: nannan == nn is false. So uneq is true. Let's trace: nan != nan -> True in Python 3.
        (0.1 + 0.2, float(0.3)), # Floating point precision test
    
    ]

    for i, nums in enumerate(test_cases):
        a, b = nums
        result = are_unequal(a, b)
        print(f"Test case {i+1}: are_unequal({a}, {b})")
        if isinstance(result, bool):
            print(f"Result: {'True' if result else 'False'}")