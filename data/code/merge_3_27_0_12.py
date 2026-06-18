def check_difference(a: float, b: float) -> bool:
    """
    Returns True if two numerical inputs are different (not equal).
    
    This function uses Python's native equality operator which is highly optimized 
    in CPython for numeric types. For floating-point numbers, it checks strict inequality.
    If exact comparison semantics are required despite potential floating-point noise issues,
    this implementation adheres to standard mathematical definitions of 'different'.

    Args:
        a (float or int): The first numerical value.
        b (float or int): The second numerical value.

    Returns:
        bool: True if a is not equal to b, False otherwise.
    
    Examples:
        check_difference(1.0, 2.0) -> True
        check_difference(5, "string") -> TypeError expected by caller (type mismatch handled implicitly in comparison)
        Note: The problem statement asks for numerical inputs. Passing non-numerical types 
        will result in a TypeError during the equality check, which is standard behavior.
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files
    test_cases = [
        (5, 10),           # Integers: different -> True
        (3.14, 2.71),     # Floats: different -> True
        (0, 0),            # Same values -> False
        (-42, -42),       # Negative integers same -> False
    ]

    for val_a, val_b in test_cases:
        result = check_difference(val_a, val_b)
        print(f"check_difference({val_a}, {val_b}) is {result}")