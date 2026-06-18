import math

def is_larger(a: float | int, b: float | int) -> bool:
    """
    Returns True if a is strictly greater than b, False otherwise.
    
    Optimized by using direct comparison which is the fastest method in Python 
    for numerical types (int and float). No unnecessary conversions or function calls are made.
    
    Args:
        a: The first number to compare.
        b: The second number to compare.
        
    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (5, 3),       # Expected: True
        (10, 10),     # Expected: False (not strictly greater)
        (-2.5, -4.5),# Expected: True
        ("abc", "def"),# Expected: TypeError expected as strings are not comparable numerically in strict numeric context but Python allows string comparison; however task implies numerical arguments. Let's stick to numbers for robustness per prompt "numerical arguments". 
    ]
    
    # Note on the last case above: The function signature type hint suggests float|int, passing non-numeric types will raise TypeError which is appropriate behavior for invalid input in a numeric context. We'll use purely numerical test cases below.

    sample_tests = [
        (100, 50),      # True
        (3.14, 2.71),   # True
        (0, -1),        # True
        (-999, -888),   # False
        (math.inf, math.nan), # NaN comparisons are always false in Python; inf > nan is false. Expected: False.
    ]

    print("Running internal tests...")
    for i, (val_a, val_b) in enumerate(sample_tests):
        result = is_larger(val_a, val_b)