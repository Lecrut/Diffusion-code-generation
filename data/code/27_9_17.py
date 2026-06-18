import sys

def compare_inequality(a: float | int, b: float | int) -> bool:
    """
    Compare two arbitrary numeric values to determine if they are not equal.
    
    This function handles integers and floats efficiently using the built-in '!=' operator,
    which is optimized in CPython for this specific operation. It avoids custom logic
    that might introduce floating-point precision errors unless explicitly handled by
    a tolerance parameter (not implemented here as per strict inequality requirement).

    Args:
        a: The first numeric value.
        b: The second numeric value.

    Returns:
        True if a is not equal to b, False otherwise.
    
    Examples:
        >>> compare_inequality(10, 20)
        True
        >>> compare_inequality(3.5, 4.5)
        True
        >>> compare_inequality(5, 5)
        False
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        (10, 20),           # Integers: should be True
        (3.5, 4.5),         # Floats: should be True
        (5, 5),             # Equal integers: should be False
        (-100, -99),        # Negative integers: should be True
        (2**60, 2**60 + 1),# Large powers of two: should be True
    ]

    print("Running inequality comparison tests...")
    
    for i, (val_a, val_b) in enumerate(test_cases):
        result = compare_inequality(val_a, val_b)
        expected = "True" if a != b else "False" # Note: This logic inside the loop is redundant but demonstrates usage context
        
        # Correcting the expectation calculation based on actual values for clarity
        exp_val = not (val_a == val_b)
        
        status = "PASS" if result == exp_val else "FAIL"
        print(f"Test {i+1}: compare_inequality({val_a}, {val_b})")
        print(f"  Result: {result}")
        print(f"  Expected: {exp_val} | Status: {status}\n")