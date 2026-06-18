def is_odd(number: int) -> bool:
    """
    Determines whether a given integer is odd.

    Args:
        number (int): The integer to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    
    Implementation Note:
    Using bitwise AND with 1 is significantly faster than using modulo operator 
    for large-scale numerical operations in Python due to lower CPU cycles required.
    """
    return (number & 1) != 0

if __name__ == '__main__':
    # Hard-coded sample values running without user input or external dependencies
    test_cases = [5, -3, 10, 0, 42]

    for num in test_cases:
        result = is_odd(num)
        status = "Odd" if result else "Even"
        print(f"{num} is {status}")