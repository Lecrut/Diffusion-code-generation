def check_parity(number):
    """
    Determines if a number is even or odd using the modulo operator.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: 'Even' if divisible by 2, otherwise 'Odd'.
    """
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or arguments.
    test_cases = [10, 7, -4, 0]

    print("Testing parity with hard-coded samples:")
    
    for num in test_cases:
        result = check_parity(num)
        print(f"{num} is {result}")