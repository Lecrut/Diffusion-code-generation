def is_zero(value):
    """
    Returns True if value is exactly zero, False otherwise.
    
    This function handles all numeric types (int, float) by converting to a common representation
    and performing an exact comparison after neutralizing floating-point noise where appropriate 
    only for the specific case of -0.0 vs 0.0, while maintaining strict equality for integers.
    For floats that are mathematically zero but have tiny non-zero representations (e.g., from calculation),
    this implementation assumes 'exactly zero' means bitwise identity to 0.0 unless specified otherwise 
    in standard numeric comparison contexts where -0.0 == 0.0 is True by IEEE 754 standards.
    
    However, given the requirement for "robust" and handling potential edge cases like NaN or signed zeros:
    We perform a direct equality check which correctly handles float comparisons including -0.0 vs 0.0 
    (both evaluate to False in an 'if value != 0:' context but True in 'value == 0' for both).
    
    Since Python's `==` operator returns True for both positive and negative zero, this satisfies the requirement.
    
    Args:
        value: A numerical argument (int or float).
        
    Returns:
        bool: True if value is exactly zero, False otherwise.
    """
    return value == 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [
        0,           # Positive integer zero -> True
        -0,          # Negative integer (same as 0) -> True
        0.0,         # Positive float zero -> True
        -0.0,        # Negative float zero -> True (IEEE 754: -0 == 0 is True in Python)
        1,           # Non-zero int -> False
        -1,          # Non-zero negative int -> False
        3.14,        # Float not equal to zero -> False
        2e-8,        # Very small float but non-zero -> False
    ]

    for test_value in samples:
        result = is_zero(test_value)
        print(f"is_zero({test_value!r}) = {result}")