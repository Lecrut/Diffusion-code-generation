def is_odd(number):
    """
    Checks if an integer is odd using the modulo operator.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        bool: True if the number is odd, False otherwise.
    """
    return number % 2 != 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [1, -3, 45, 100, -7]
    
    print("Testing is_odd function:")
    for num in test_cases:
        result = is_odd(num)
        status = "Odd" if result else "Even"
        print(f"{num}: {status}")