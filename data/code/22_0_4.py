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
    test_numbers = [1, -5, 42, 0]

    print("Testing parity determination with hard-coded samples:")
    
    for num in test_numbers:
        result = determine_parity(num)
        print(f"The number {num} is {result}.")