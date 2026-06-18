def is_positive(number: float) -> bool:
    """
    Returns True if the number is strictly positive, False otherwise.
    
    Args:
        number (float): A numerical value to be checked.
        
    Returns:
        bool: The result of checking whether the number is greater than zero.

    Raises:
        TypeError: If 'number' is not a float or int type.
    """
    if not isinstance(number, (int, float)):
        raise TypeError("Expected an integer or float.")
    
    return number > 0

if __name__ == '__main__':
    test_cases = [1.5, -3, 0, 42]
    for value in test_cases:
        result = is_positive(value)
        print(f"is_positive({value}) = {result}")