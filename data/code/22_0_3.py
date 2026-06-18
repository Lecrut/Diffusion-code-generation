def determine_parity(number):
    """
    Determines whether a given integer is odd or even.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: 'odd' if the number is odd, 'even' otherwise.
    """
    return "odd" if number % 2 != 0 else "even"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments
    test_values = [10, 7, -3, 0]

    print("Testing parity determination with hard-coded samples:")
    
    for value in test_values:
        result = determine_parity(value)
        print(f"The number {value} is {result}.")