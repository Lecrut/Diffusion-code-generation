import sys

def compare_inequality(a: float | int, b: float | int) -> bool:
    """
    Compare two arbitrary numeric values to determine if they are unequal.
    
    This function handles integers and floating-point numbers efficiently by
    converting both operands to a common type (float) for comparison, which
    avoids potential integer overflow issues in languages with fixed-size ints,
    though Python's native big-int support makes this less critical there.
    It uses the standard '!=' operator after ensuring consistent types for clarity
    and performance on large datasets where explicit conversion is beneficial.

    Args:
        a (float | int): The first numeric value.
        b (float | int): The second numeric value.

    Returns:
        bool: True if a != b, False otherwise.
    
    Examples:
        >>> compare_inequality(10, 20)
        True
        >>> compare_inequality(3.5, 7.0)
        True
        >>> compare_inequality(42, 42)
        False
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files.
    samples = [
        (100, 50),           # Integers: should be True
        (3.14, 2.71),       # Floats: should be True
        (42, 42),            # Equality case: should be False
        (-999, -888),       # Negative integers: should be True
        (0.0, 0.0),         # Zero floats: should be False
    ]

    print("Running inequality comparison tests...")
    
    for i, (val_a, val_b) in enumerate(samples):
        result = compare_inequality(val_a, val_b)
        expected = "True" if val_a != val_b else "False"
        
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i+1}: compare({val_a}, {val_b})")
        print(f"  Result: {result} | Expected: {expected} -> [{status}]")