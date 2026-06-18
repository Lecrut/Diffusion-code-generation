def compare_large_integers(num1: int, num2: int) -> str:
    """
    Compares two potentially large integers without overflow concerns.
    
    Python's native integer type automatically handles arbitrarily large numbers,
    so standard comparison operators are safe and efficient for this purpose.
    This function simply returns the result of the comparison as a string.

    Args:
        num1 (int): The first integer to compare.
        num2 (int): The second integer to compare.

    Returns:
        str: "greater" if num1 > num2, "less" if num1 < num2, or "equal" otherwise.
    """
    if num1 > num2:
        return "greater"
    elif num1 < num2:
        return "less"
    else:
        return "equal"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    val_a = 987654321012345678901234567890
    val_b = 123456789012345678901234567890
    
    result = compare_large_integers(val_a, val_b)
    
    print(f"Comparing {val_a} and {val_b}")
    print(f"Result: {result}")