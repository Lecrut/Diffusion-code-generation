def is_odd(n: int) -> bool:
    """
    Returns True if n is odd, False otherwise.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is odd, False otherwise.
    
    Note: This implementation uses the modulo operator for clarity and efficiency in Python.
    """
    return n % 2 != 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or files
    test_cases = [1, -5, 42, 0, 999]

    for num in test_cases:
        result = is_odd(num)
        print(f"is_odd({num}) = {result}")